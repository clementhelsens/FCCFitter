import glob
import optparse
import subprocess
import sys
import json
import os
import ROOT as r

#__________________________________________________________
def createdict(name):
    if not fexist(name):
        print 'dictionnary ', name, ' does not exist. Create it'
        file_handle = open(name,"w")
        file_handle.write('{}\n')
        file_handle.close()
        mydict = None
    with open(name) as f:
        mydict = json.load(f)
    return mydict


#__________________________________________________________
def fexist(name):
    if not os.path.exists(name): return False
    return True


#__________________________________________________________
def pointexits(mydict, mass, lumi):
    if len(mydict)==0:return False
    for m in mydict:
        if m==mass: 
            for j in mydict[mass]:
                if lumi==int(j['lumi']): return True
        return False

#__________________________________________________________
def setconfig(cfg, lumi):
#set lumi in pb-1
    outdir=''
    job=''
    with open(cfg) as f:
        infile = f.readlines()
        for line in xrange(len(infile)):
            if 'MultiFit:' in infile[line] :
                print 'Joboptions seems to be combined, you used the wrong option, exit'
                sys.exit(3)
            if 'Lumi:' in infile[line] :
                infile[line]='  Lumi:%.3f\n'%lumi
            if 'OutputDir:' in infile[line] :
                infile[line]=infile[line].replace('Outputs','Outputs_signi')
                outdir=infile[line].split(':')
                outdir=outdir[1].replace('\n','')
            if "Job:" in infile[line] :
                job=infile[line].split(':')
                job=job[1].replace(' ','').replace('"','').replace('\n','')
    with open(cfg.replace('.config','_signi.config'), "w") as f1:
        f1.writelines(infile) 
    return outdir,job


#__________________________________________________________
def setconfigcomb(cfg, lumi):
#set lumi in pb-1
    outdir=''
    job=''
    subconf=[]
    with open(cfg) as f:
        infile = f.readlines()
        for line in xrange(len(infile)):
            if 'Job:' in infile[line] :
                print 'Joboptions seems to be not combined, you used the wrong option, exit'
                sys.exit(3)

            if 'OutputDir:' in infile[line] :
                infile[line]=infile[line].replace('Outputs','Outputs_signi')
                outdir=infile[line].split(':')
                outdir=outdir[1].replace('\n','')

            if "ConfigFile:" in infile[line] :
                tmpjob=infile[line].replace('ConfigFile:','').replace(' ','').replace('\n','')
                print '===============================%s==============================='%tmpjob
                subconf.append(tmpjob)
                setconfig(tmpjob, lumi)
                infile[line]=infile[line].replace('.config','_signi.config')
                
            if "MultiFit:" in infile[line] :
                job=infile[line].split(':')
                job=job[1].replace(' ','').replace('"','').replace('\n','')
    with open(cfg.replace('.config','_signi.config'), "w") as f1:
        f1.writelines(infile) 
    return outdir,job,subconf

#__________________________________________________________
def excecuteShell(cmd):
    p=subprocess.Popen(cmd, shell=True)
    p.communicate()


#__________________________________________________________
def addpoint(mydict, mass, lumi, signi):
    if pointexits(mydict, mass, lumi):
        return
    exist=False
    for m in mydict:
        if m==mass: 
            exist=True
            mydict[mass].append({'lumi':lumi,'signi':signi})
    if not exist:
        mydict[mass]=[{'lumi':lumi,'signi':signi}]
    return


#__________________________________________________________
def write(outname,mydict):
    with open(outname, 'w') as f:
        json.dump(mydict, f)
    return


#__________________________________________________________
def getSigni(cfg, lumi,combined):
    outdir=''
    job=''
    subconf=None
    if not combined: outdir,job=setconfig(cfg,lumi)
    else:            outdir,job,subconf=setconfigcomb(cfg,lumi)

    print '================  ',outdir
    print '================  ',job
    mass=cfg.split('_')
    mass=[mass[i].replace('TeV.config','').replace('TeV','') for i in xrange(len(mass)) if 'TeV' in mass[i]]
    if len(mass)==1:mass=mass[0]
    
    if not combined:
        cmd="./myFit.exe hwfs %s"%(cfg.replace('.config','_signi.config'))
        excecuteShell(cmd)
      
        cmd='rm %s'%(cfg.replace('.config','_signi.config'))
        excecuteShell(cmd)

    else:
        for s in subconf:
            cmd="./myFit.exe hw %s"%(s.replace('.config','_signi.config'))
            excecuteShell(cmd)

        cmd="./myFit.exe mwfs %s"%(cfg.replace('.config','_signi.config'))
        excecuteShell(cmd)
      
        cmd='rm %s'%(cfg.replace('.config','_signi.config'))
        excecuteShell(cmd)
        for s in subconf:
            cmd='rm %s'%(s.replace('.config','_signi.config'))
            excecuteShell(cmd)

    signi = r.TFile.Open('%s/%s/Significance/%s.root'%(outdir,job,job))
    print '%s/%s/Significance/%s.root'%(outdir,job,job)
    histo = signi.Get("hypo")
    signi = histo.GetBinContent(2)
    print '---------------------------- signi   ',signi
    print '---------------------------- lumi    ',lumi


    addpoint(mydict, mass, lumi, signi)
    write(name,mydict)
    return signi


#__________________________________________________________
if __name__=="__main__":
    
    parser = optparse.OptionParser(description="analysis parser")
    parser.add_option('-f', '--file', dest='files', type=str, default='', help='input files')
    parser.add_option('-n', '--n', dest='name', type=str, default='default',help='name of the output json file with signi and lumi for all masses')
    parser.add_option("-c", "--combined",action="store_true", dest="combined", default=False, help='run combined fit')
    parser.add_option("-e","--exclude", type=str, default='',help="exclude pattern for glob")
    ops, args = parser.parse_args()
    config_files=glob.glob(ops.files)

    if ops.exclude!='':
        config_files=[f for f in config_files if ops.exclude not in f]
        
    name = ops.name
    combined=ops.combined
    if not os.path.isdir("Data/"):
        os.system('mkdir Data')
    if '.json' not in name:name='Data/'+name+'.json'
    else: name='Data/'+name

    config_files = [i for i in config_files if '~' not in i and 'signi' not in i]
    print config_files

    mydict=createdict(name)

    nsig=10
    nsigstart=0
    lumies_high=[1, 2, 4, 7, 10]
    lumies_low=[0.05, 0.1, 0.2, 0.5]

    lumistart=10
    tobreak=False
    for cfg in config_files:
        signi=getSigni(cfg, lumistart,combined)
        scaling=(nsig/signi)**2
        print 'scaling  ',scaling

        for l in xrange(len(lumies_high)):
            signi=getSigni(cfg, lumies_high[l]*scaling,combined)
            if signi>nsig and l==0:
                tobreak=True
                for l2 in xrange(len(lumies_low)):
                    signi=getSigni(cfg, lumies_low[l2]*scaling,combined)
            if tobreak: break
        import time
        time.sleep(3)
        
