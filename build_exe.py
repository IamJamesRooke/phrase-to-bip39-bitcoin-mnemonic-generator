# filepath: c:\Users\james\OneDrive\Code\phrase2bip39\build_exe.py
import PyInstaller.__main__
import os
import sys

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
    
    # PyInstaller arguments
    args = [
        '--onefile',  # Create a single executable file
        '--console',  # Keep console window (needed for input/output)
        '--name=Phrase2BIP39',  # Name of the executable
        '--distpath=dist',  # Output directory
        '--workpath=build',  # Build directory
        '--specpath=.',  # Spec file location
        '--clean',  # Clean PyInstaller cache
        main_script
    ]
    
    print("Building executable with PyInstaller...")
    print(f"Source file: {main_script}")
    print("This may take a few minutes...")
    
    try:
        PyInstaller.__main__.run(args)
        
        # Check if build was successful
        exe_path = os.path.join(script_dir, "dist", "Phrase2BIP39.exe")
        if os.path.exists(exe_path):
            print(f"\n✅ SUCCESS! Executable created at:")
            print(f"   {exe_path}")
            print(f"\nFile size: {os.path.getsize(exe_path) / (1024*1024):.1f} MB")
            return True
        else:
            print("❌ Build completed but executable not found!")
            return False
            
    except Exception as e:
        print(f"❌ Error during build: {e}")
        return False

if __name__ == "__main__":
    print("=" * 60)
    print("PHRASE2BIP39 EXECUTABLE BUILDER")
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
            print("Your executable is ready to use.")
            print("You can now distribute the .exe file without")
            print("requiring Python to be installed on the target computer.")
            print()
            print("The executable includes:")
            print("• Your Python script")
            print("• Python interpreter")
            print("• All required libraries")
            print()
        else:
            print("\n" + "=" * 60)
            print("BUILD FAILED!")
            print("=" * 60)
            print()
            print("Check the error messages above for details.")
    else:
        print("Build cancelled.")
    
    input("\nPress Enter to exit...")