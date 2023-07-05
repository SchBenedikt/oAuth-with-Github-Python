import subprocess

# List of required Python dependencies
required_dependencies = ["flask", "requests", "authlib"]

def install_dependencies():
    for dependency in required_dependencies:
        try:
            subprocess.run(["pip", "install", dependency], check=True)
            print(f"Successfully installed {dependency}.")
        except subprocess.CalledProcessError as e:
            print(f"Error installing {dependency}.")
            print(e)
            break

if __name__ == "__main__":
    print("Installing required Python dependencies...")
    install_dependencies()
    print("All dependencies have been installed.")
