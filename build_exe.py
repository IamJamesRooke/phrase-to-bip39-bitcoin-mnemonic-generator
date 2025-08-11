# filepath: c:\Users\james\OneDrive\Code\phrase2bip39\build_exe.py
import PyInstaller.__main__
import os
import sys
import shutil

# Version Information
VERSION = "1.0.1"
SCRIPT_NAME = "Phrase2BIP39 Executable Builder"

def clean_directories(script_dir):
    """Clean up build and dist directories"""
    build_dir = os.path.join(script_dir, "build")
    dist_dir = os.path.join(script_dir, "dist")
    
    for directory in [build_dir, dist_dir]:
        if os.path.exists(directory):
            try:
                # Try multiple times with different approaches
                import time
                for attempt in range(3):
                    try:
                        shutil.rmtree(directory)
                        print(f"🧹 Cleaned up {os.path.basename(directory)} folder")
                        break
                    except PermissionError:
                        if attempt < 2:
                            print(f"⏳ Retrying cleanup of {os.path.basename(directory)}... (attempt {attempt + 2})")
                            time.sleep(1)
                        else:
                            print(f"⚠️  Warning: Could not remove {directory} (permission denied)")
                            print(f"   You can manually delete this folder later")
                    except Exception as e:
                        print(f"⚠️  Warning: Could not remove {directory}: {e}")
                        break
            except Exception as e:
                print(f"⚠️  Warning: Could not remove {directory}: {e}")

def build_executable():
    """
    Build an executable from the phrase2bip39.py script using PyInstaller
    """
    
    # Get the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Path to the main Python file
    main_script = os.path.join(script_dir, "phrase2bip39.py")
    
    # Check if the main script exists
    if not os.path.exists(main_script):
        print(f"Error: {main_script} not found!")
        return False
    
    # Clean up any existing build artifacts first
    print("🧹 Pre-cleaning build directories...")
    clean_directories(script_dir)
    
    # PyInstaller arguments - output directly to root folder
    args = [
        '--onefile',  # Create a single executable file
        '--console',  # Keep console window (needed for input/output)
        '--name=phrase2BIP39',  # Name of the executable
        '--distpath=.',  # Output to root directory
        '--workpath=build',  # Build directory (will be cleaned up)
        '--specpath=.',  # Spec file location
        '--noconfirm',  # Don't ask for confirmation to overwrite
        main_script
    ]
    
    print("Building executable with PyInstaller...")
    print(f"Source file: {main_script}")
    print("This may take a few minutes...")
    
    try:
        PyInstaller.__main__.run(args)
        
        # Check if build was successful - exe should be in root folder now
        exe_path = os.path.join(script_dir, "phrase2BIP39.exe")
        if os.path.exists(exe_path):
            print(f"\n✅ SUCCESS! Executable created at:")
            print(f"   {exe_path}")
            print(f"\nFile size: {os.path.getsize(exe_path) / (1024*1024):.1f} MB")
            
            # Clean up build folders
            print()
            clean_directories(script_dir)
            
            # Remove spec file if it exists
            spec_file = os.path.join(script_dir, "phrase2BIP39.spec")
            if os.path.exists(spec_file):
                try:
                    os.remove(spec_file)
                    print("🧹 Cleaned up spec file")
                except Exception as e:
                    print(f"⚠️  Warning: Could not remove spec file: {e}")
            
            return True
        else:
            print("❌ Build completed but executable not found!")
            return False
            
    except Exception as e:
        print(f"❌ Error during build: {e}")
        print("\n💡 Try running as administrator or:")
        print("   1. Close any antivirus real-time scanning")
        print("   2. Make sure no other programs are using the files")
        print("   3. Try running the command in a clean terminal")
        return False

if __name__ == "__main__":
    print("=" * 60)
    print(f"{SCRIPT_NAME} v{VERSION}")
    print("=" * 60)
    print()
    print("This script will create a standalone .exe file")
    print("from your phrase2bip39.py script.")
    print()
    print("Requirements:")
    print("• PyInstaller must be installed")
    print("• All dependencies must be available")
    print()
    
    # Check if PyInstaller is available
    try:
        import PyInstaller
        print("✅ PyInstaller found")
    except ImportError:
        print("❌ PyInstaller not found!")
        print("\nTo install PyInstaller, run:")
        print("   pip install pyinstaller")
        input("\nPress Enter to exit...")
        sys.exit(1)
    
    # Check for required dependencies
    try:
        import mnemonic
        print("✅ mnemonic library found")
    except ImportError:
        print("❌ mnemonic library not found!")
        print("\nTo install mnemonic, run:")
        print("   pip install mnemonic")
        input("\nPress Enter to exit...")
        sys.exit(1)
    
    print()
    response = input("Continue with build? (y/n): ").lower().strip()
    
    if response in ['y', 'yes']:
        print()
        success = build_executable()
        
        if success:
            print("\n" + "=" * 60)
            print("BUILD COMPLETE!")
            print("=" * 60)
            print()
            print("Your executable (phrase2BIP39.exe) is ready in the root folder.")
            print("You can now distribute the .exe file without")
            print("requiring Python to be installed on the target computer.")
            print()
            print("The executable includes:")
            print("• Your Python script")
            print("• Python interpreter") 
            print("• All required libraries")
            print()
            print("✨ Clean setup: No build/dist folders left behind!")
        else:
            print("\n" + "=" * 60)
            print("BUILD FAILED!")
            print("=" * 60)
            print()
            print("Check the error messages above for details.")
    else:
        print("Build cancelled.")
    
    input("\nPress Enter to exit...")