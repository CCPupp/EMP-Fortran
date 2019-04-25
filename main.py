import      pip
import      subprocess
import      sys
import      time
import      d

def install(package):
    subprocess.call([sys.executable, "-m", "pip", "install", package])

# Example
if __name__ == '__main__':
    print("Checking for Scipy install...")
    time.sleep(1)
    install('scipy-stack')
    d.d()