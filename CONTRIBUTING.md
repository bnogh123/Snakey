# Contributing to Snakey Dashboard

Thank you for your interest in contributing to the Snakey Dashboard! This document provides guidelines for contributing to the project.

## How to Contribute

### Reporting Bugs

If you find a bug, please open an issue with:
- A clear, descriptive title
- Steps to reproduce the issue
- Expected vs actual behavior
- Screenshots if applicable
- Your environment (OS, browser, Python version)

### Suggesting Enhancements

Enhancement suggestions are welcome! Please open an issue with:
- A clear description of the enhancement
- Why this enhancement would be useful
- Potential implementation approach

### Pull Requests

1. **Fork the repository** and create your branch from `main`
2. **Make your changes**:
   - Follow the existing code style
   - Add comments for complex logic
   - Update documentation as needed
3. **Test your changes**:
   - Run the app locally to verify it works
   - Check all visualizations load correctly
   - Ensure no errors in the console
4. **Commit your changes**:
   - Use clear, descriptive commit messages
   - Reference related issues (e.g., "Fixes #123")
5. **Push to your fork** and submit a pull request

## Development Setup

1. Clone your fork:
   ```bash
   git clone https://github.com/YOUR_USERNAME/Snakey.git
   cd Snakey
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the app:
   ```bash
   python app.py
   ```

## Code Style Guidelines

### Python
- Follow PEP 8 style guide
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Keep functions focused and single-purpose

### Data Files (CSV)
- Use UTF-8 encoding
- Include headers
- Use consistent formatting
- Document data sources in comments or separate documentation

### Visualizations
- Use consistent color schemes (refer to `config.py`)
- Add clear titles and labels
- Include helpful tooltips with `hover_data`
- Test on different screen sizes

## Areas for Contribution

### High Priority
- Additional snake species data (especially from underrepresented regions)
- More media appearances and cultural references
- Updated conservation status information
- Performance optimizations for large datasets

### Medium Priority
- New visualization types
- Additional filtering and search capabilities
- Mobile responsiveness improvements
- Accessibility enhancements

### Ideas Welcome
- Interactive range maps for species
- Snake bite statistics and medical information
- Educational resources and fact sheets
- Multi-language support

## Data Contributions

When adding or updating data:

1. **Verify accuracy**: Use reputable sources
2. **Cite sources**: Add references in documentation
3. **Maintain format**: Follow existing CSV structure
4. **Test thoroughly**: Ensure new data loads and displays correctly

### Data Sources Guidelines
Acceptable sources include:
- Peer-reviewed scientific literature
- Government wildlife agencies
- Reputable conservation organizations (IUCN, etc.)
- Academic institutions
- Verified media databases (IMDB, etc.)

## Documentation

When updating documentation:
- Use clear, concise language
- Include examples where helpful
- Update README.md if adding new features
- Add comments to complex code

## Questions?

If you have questions about contributing:
- Check existing issues and pull requests
- Open a new issue with the "question" label
- Be patient and respectful

## Code of Conduct

### Our Standards

- Be respectful and inclusive
- Accept constructive criticism gracefully
- Focus on what's best for the project
- Show empathy towards others

### Unacceptable Behavior

- Harassment or discriminatory language
- Trolling or insulting comments
- Publishing others' private information
- Other unprofessional conduct

## License

By contributing to Snakey Dashboard, you agree that your contributions will be licensed under the MIT License.

---

Thank you for contributing to making snake education more accessible and accurate!
