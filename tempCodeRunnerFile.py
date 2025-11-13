import subprocess
import sys

# List of all essential packages for EDA
packages = [
    "pandas",
    "numpy",
    "matplotlib",
    "seaborn",
    "scipy",
    "statsmodels",
    "openpyxl",
    "xlrd",
    "pyarrow",
    "scikit-learn",
    "jupyter",
    "notebook",
    "ipykernel",
    "tqdm",
    "requests",
    "python-dotenv"
]

def install_packages(pkg_list):
    for pkg in pkg_list:
        try:
            print(f"🔹 Installing {pkg} ...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", pkg])
        except subprocess.CalledProcessError:
            print(f"❌ Failed to install {pkg}")
        else:
            print(f"✅ {pkg} installed successfully\n")

if __name__ == "__main__":
    print("🚀 Starting package installation...")
    install_packages(packages)
    print("\n🎯 All installations attempted. You’re ready for EDA!")
