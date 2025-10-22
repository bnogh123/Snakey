"""
Test script to verify Snakey dashboard installation
Run this before starting the app to check if everything is set up correctly
"""

import sys
import os

def test_python_version():
    """Check Python version"""
    print("Testing Python version...")
    version = sys.version_info
    if version.major >= 3 and version.minor >= 9:
        print(f"[OK] Python {version.major}.{version.minor}.{version.micro}")
        return True
    else:
        print(f"[FAIL] Python {version.major}.{version.minor}.{version.micro} (Need 3.9+)")
        return False

def test_imports():
    """Test if required packages can be imported"""
    print("\nTesting package imports...")
    packages = {
        'dash': 'Dash',
        'dash_bootstrap_components': 'Dash Bootstrap Components',
        'plotly': 'Plotly',
        'pandas': 'Pandas',
        'numpy': 'NumPy'
    }

    all_ok = True
    for package, name in packages.items():
        try:
            __import__(package)
            print(f"[OK] {name}")
        except ImportError:
            print(f"[FAIL] {name} (NOT FOUND)")
            all_ok = False

    return all_ok

def test_data_files():
    """Check if all required data files exist"""
    print("\nTesting data files...")
    data_files = [
        'data/raw/us_snake_species.csv',
        'data/raw/global_snake_species.csv',
        'data/raw/domesticated_snakes.csv',
        'data/raw/snakes_in_media.csv',
        'data/raw/snakeskin_farming.csv'
    ]

    all_ok = True
    for file_path in data_files:
        if os.path.exists(file_path):
            size = os.path.getsize(file_path)
            print(f"[OK] {file_path} ({size:,} bytes)")
        else:
            print(f"[FAIL] {file_path} (NOT FOUND)")
            all_ok = False

    return all_ok

def test_project_structure():
    """Check if project structure is correct"""
    print("\nTesting project structure...")
    required_items = [
        ('app.py', 'file'),
        ('config.py', 'file'),
        ('requirements.txt', 'file'),
        ('src/', 'dir'),
        ('src/pages/', 'dir'),
        ('src/utils/', 'dir'),
        ('data/raw/', 'dir'),
    ]

    all_ok = True
    for item, item_type in required_items:
        if item_type == 'file':
            exists = os.path.isfile(item)
        else:
            exists = os.path.isdir(item)

        if exists:
            print(f"[OK] {item}")
        else:
            print(f"[FAIL] {item} (NOT FOUND)")
            all_ok = False

    return all_ok

def test_data_loading():
    """Test if data can be loaded"""
    print("\nTesting data loading...")
    try:
        from src.utils.data_loader import (
            load_us_snakes,
            load_global_snakes,
            load_domesticated_snakes,
            load_media_snakes,
            load_farming_data
        )

        datasets = {
            'US Snakes': load_us_snakes,
            'Global Snakes': load_global_snakes,
            'Domesticated Snakes': load_domesticated_snakes,
            'Media Snakes': load_media_snakes,
            'Farming Data': load_farming_data
        }

        all_ok = True
        for name, loader in datasets.items():
            try:
                df = loader()
                print(f"[OK] {name} ({len(df)} records)")
            except Exception as e:
                print(f"[FAIL] {name} (ERROR: {str(e)})")
                all_ok = False

        return all_ok
    except Exception as e:
        print(f"[FAIL] Could not import data loaders: {str(e)}")
        return False

def main():
    """Run all tests"""
    print("="*60)
    print("Snakey Dashboard - Installation Test")
    print("="*60)

    tests = [
        test_python_version,
        test_imports,
        test_project_structure,
        test_data_files,
        test_data_loading
    ]

    results = []
    for test in tests:
        results.append(test())

    print("\n" + "="*60)
    print("Test Summary")
    print("="*60)

    if all(results):
        print("[SUCCESS] All tests passed! You're ready to run the dashboard.")
        print("\nRun the dashboard with:")
        print("  python app.py")
        print("\nThen open your browser to:")
        print("  http://localhost:8050")
    else:
        print("[FAILED] Some tests failed. Please fix the issues above.")
        print("\nCommon fixes:")
        print("  - Install packages: pip install -r requirements.txt")
        print("  - Ensure you're in the correct directory")
        print("  - Activate virtual environment")

    print("="*60)

if __name__ == '__main__':
    main()
