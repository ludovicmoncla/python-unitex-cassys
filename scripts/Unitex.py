import os
import shutil
import argparse
from subprocess import DEVNULL, STDOUT, check_call


class Unitex:

    def __init__(self, version="Standard", lang="French", install_path=None, install_path_app=None, delete_tmp_files=True):
        self.version = version
        self.lang = lang
        self.delete_tmp_files = delete_tmp_files
        
        self.install_path = install_path
        self.install_path_app = install_path_app


    def run(self, filepath):
        analysis_cascade = os.path.join('CasSys', self.version, 'analysis.csc')
        synthesis_cascade = os.path.join('CasSys', self.version, 'synthesis.csc')
        # preprocessing needed, if use of dictionnaries
        #unitex.run_preprocessing(filepath)
        self.run_cascade(filepath, analysis_cascade, "")
        self.run_cascade(filepath, synthesis_cascade, "_csc")
        self.csc2xml(filepath, "-utf8", "_csc_csc")

        #TODO: add root to xml file
        #TODO: add a return value (xml content)


    def run_preprocessing(self, file_path):

        cmd = self.install_path_app + "/UnitexToolLogger Grf2Fst2 " + self.install_path + "/" + self.lang + "/Graphs/Preprocessing/Sentence/Sentence.grf"
        cmd += " -y --alphabet=" + self.install_path + "/" + self.lang + "/Alphabet.txt"
        cmd += " -d " + self.install_path + "/" + self.lang + "/Graphs"
        #os.system(cmd + " > /dev/null")
        check_call(list(cmd.split(" ")), stdout=DEVNULL, stderr=STDOUT)

        cmd = self.install_path_app + "/UnitexToolLogger Flatten " + self.install_path + "/" + self.lang + "/Graphs/Preprocessing/Sentence/Sentence.fst2 --rtn -d5"
        #os.system(cmd + " > /dev/null")
        check_call(list(cmd.split(" ")), stdout=DEVNULL, stderr=STDOUT)

        cmd = self.install_path_app + "/UnitexToolLogger Fst2Txt -t" + file_path + ".snt " + self.install_path + "/" + self.lang + "/Graphs/Preprocessing/Sentence/Sentence.fst2 -a"
        cmd += self.install_path + "/"+ self.lang+"/Alphabet.txt -M"
        #os.system(cmd + " > /dev/null")
        check_call(list(cmd.split(" ")), stdout=DEVNULL, stderr=STDOUT)

        cmd = self.install_path_app + "/UnitexToolLogger Grf2Fst2 " + self.install_path + "/" + self.lang+"/Graphs/Preprocessing/Replace/Replace.grf"
        cmd += " -y --alphabet=" + self.install_path + "/"+ self.lang+"/Alphabet.txt"
        cmd += " -d " + self.install_path + "/" + self.lang + "/Graphs"
        #os.system(cmd + " > /dev/null")
        check_call(list(cmd.split(" ")), stdout=DEVNULL, stderr=STDOUT)

        cmd = self.install_path_app + "/UnitexToolLogger Fst2Txt -t" + file_path + ".snt " + self.install_path + "/" + self.lang+"/Graphs/Preprocessing/Replace/Replace.fst2"
        cmd += " -a" + self.install_path + "/" + self.lang+"/Alphabet.txt -R"
        #os.system(cmd + " > /dev/null")
        check_call(list(cmd.split(" ")), stdout=DEVNULL, stderr=STDOUT)
        
    def load_dictionnaries(self):
        pass


    def run_cascade(self, file_path, cascade_path, suffix):
        try:
            os.mkdir(file_path + suffix + "_snt")
        except:
            pass


        cmd = self.install_path_app + "/UnitexToolLogger Normalize " + file_path + suffix + ".txt -r" + self.install_path + "/" + self.lang + "/Norm.txt"
        #os.system(cmd + " > /dev/null")
        check_call(list(cmd.split(" ")), stdout=DEVNULL, stderr=STDOUT)
        
        cmd = self.install_path_app + "/UnitexToolLogger Tokenize " + file_path + suffix + ".snt -a" + self.install_path + "/" + self.lang + "/Alphabet.txt"
        #os.system(cmd + " > /dev/null")
        check_call(list(cmd.split(" ")), stdout=DEVNULL, stderr=STDOUT)

        cmd = self.install_path_app + "/UnitexToolLogger Cassys -a" + self.install_path + "/" + self.lang + "/Alphabet.txt"
        cmd += " -t" + file_path + suffix + ".snt -l" + self.install_path+ "/" + self.lang + "/" + cascade_path + " -v -r" + self.install_path + "/" + self.lang + "/Graphs/"
        #os.system(cmd + " > /dev/null")
        check_call(list(cmd.split(" ")), stdout=DEVNULL, stderr=STDOUT)

        if self.delete_tmp_files:
            try:
                shutil.rmtree(file_path + suffix + "_snt")
                shutil.rmtree(file_path + suffix)
                shutil.rmtree(file_path + suffix + suffix)
            except:
                pass
            try:
                if suffix != "":
                    os.remove(file_path + suffix + ".txt")
            except:
                pass
            try:
                os.remove(file_path + suffix + ".snt")
            except:
                pass
            try:
                os.remove(file_path + suffix + ".raw")
                os.remove(file_path + suffix + suffix + ".raw")
            except:
                pass


    def csc2xml(self, file_path, suffix, suffix2):

        cmd = self.install_path_app + "/UnitexToolLogger Convert -s" + self.lang.upper() + " -dUTF-8 --ss="+suffix+" " + file_path + suffix2 + ".txt"
        #os.system(cmd + " > /dev/null")
        check_call(list(cmd.split(" ")), stdout=DEVNULL, stderr=STDOUT)
        if self.delete_tmp_files:
            try:
                os.remove(file_path + suffix2 + ".txt")
            except:
                pass


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Run cascade Unitex')
    parser.add_argument('-c', '--cascade', 
                        dest='cascade_name', 
                        default='',
                        help='name of the cascade')
    parser.add_argument('-l', '--lang', 
                        dest='lang', 
                        default='English',
                        help='language')
    parser.add_argument('-i', '--input', 
                        dest='input_filepath', 
                        help='input filepath without the extension')
    parser.add_argument('--install_path', 
                        dest='install_path', 
                        help='install path of Unitex where Graphs and Cassys directories are stored')
    parser.add_argument('--install_path_app', 
                        dest='install_path_app', 
                        help='install path of the App directory of Unitex')
    args = parser.parse_args()

    delete_tmp_files = True    
    unitex = Unitex(args.cascade_name, args.lang, args.install_path, args.install_path_app, delete_tmp_files)
    unitex.run(args.input_filepath)


