import json
import shutil
import os
class TestCaseGenerator():
    def __init__(self,confPath,log=True):
        self.readConfs(confPath)

    def readConfs(self,confPath):
        f = open(confPath, "r")
        self.confs=json.loads(f.read())
        f.close()
    def creatDirectories(self):
        inPath=os.path.join(self.confs["destination"],"in")
        outPath=os.path.join(self.confs["destination"],"out")
        if os.path.exists(inPath):
            shutil.rmtree(inPath)
        if os.path.exists(outPath):
            shutil.rmtree(outPath)
        os.makedirs(inPath)
        os.makedirs(outPath)

    def writeInput(self,index):
        f=open(os.path.join(self.confs["destination"],"in","input"+str(index+1)+".txt"),'w')
        f.write(self.confs["test_cases"][index])
        f.close()

    def generateCommand(self,index):
        return self.confs["execute"]+\
               ' "'+self.confs["executable_file"]+\
               '" < "'+os.path.join(self.confs["destination"],"in","input"+str(index+1)+".txt")\
               +'" > "'+os.path.join(self.confs["destination"],"out","output"+str(index+1)+".txt")+'"'
    def zip(self):
        os.system("cd "+self.confs["destination"]+"; zip -r "+self.confs["zip_name"]+'.zip in out')
    def generate(self):
        self.creatDirectories()
        for i in range(len(self.confs["test_cases"])):
            self.writeInput(i)
            os.system(self.generateCommand(i))
        self.zip()
        shutil.rmtree(os.path.join(self.confs["destination"],"in"))
        shutil.rmtree(os.path.join(self.confs["destination"],"out"))
    def readTestCase(self):
        path = os.path.join(self.confs["destination"],self.confs["zip_name"]+'.zip') if self.confs['extract']==1 else self.confs['extract']
        if os.path.exists('___tmp___'):
            shutil.rmtree('___tmp___')
        os.mkdir("___tmp___")
        os.system('unzip '+path+' -d ___tmp___')
        outFiles = sorted([f for f in os.listdir('___tmp___/out') if os.path.isfile(os.path.join('___tmp___/out', f))])
        inFiles = sorted([f for f in os.listdir('___tmp___/in') if os.path.isfile(os.path.join('___tmp___/in', f))])
        print('<<<<<<<-------------        ------------>>>>>>>')
        for i in range(len(outFiles)):
            f=open('___tmp___/in/'+inFiles[i],'r')
            print('input'+str(i+1)+':',f.read(),'\n===========')
            f.close()
            f = open('___tmp___/out/' + outFiles[i], 'r')
            print('output'+str(i+1)+':', f.read(), '\n===========')
            f.close()
            print('<<<<<<<-------------        ------------>>>>>>>')
        shutil.rmtree("___tmp___")

test=TestCaseGenerator("confs.json")
test.generate()
test.readTestCase()