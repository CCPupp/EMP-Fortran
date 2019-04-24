import  convo 
import      dawson 
#import      gamma 
import      isomer 
import      ngamma
import      prompt 
import      source 
import      sourcen
import      pip
import      subprocess
import      sys
import      time

def install(package):
    subprocess.call([sys.executable, "-m", "pip", "install", package])

# Example
if __name__ == '__main__':
    print("Checking for Scipy install...")
    time.sleep(1)
    install('scipy-stack')