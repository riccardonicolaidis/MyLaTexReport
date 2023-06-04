# The **Latex Document Python Class** for report generation

## Introduction
`LatexDocumentClass` is a Python class for generating LaTeX documents using the Beamer package. It provides convenient methods to set the document properties, build the document structure, create slides, itemize lists, insert figures, and compile the document.

## Installation

No installation is required. Simply copy the `LatexDocumentClass` class into your Python project.

## Usage

1. Create an instance of `LatexDocumentClass`:

```python
document = LatexDocumentClass()

```

2. Set the document properties:

```python
document.SetNameOfTheDocument("MyDocument")
document.SetTitle("My Title")
document.SetAuthor("John Doe")
document.SetEmail("john.doe@example.com")
document.SetOutputDirectory("./Output/")
```

3. Build the document structure:

    - Complete the **Body** of the document as you wish:

    ```python
    document.Body += r""" Text ... """
    ```
    - Add a **Slide**:

    ```python
    document.BeginSlide("Slide Title")
    document.Body += r""" Text ... """
    document.BeginItemize()
    document.AddItem("Item 1")
    document.AddItem("Item 2")
    document.EndItemize()
    document.EndSlide()
    ```
    - Add a **Figure**:

    ```python
    document.BeginSlide("Slide Title")
    document.Body += r""" Text ... """
    document.InsertFigure(<Path Figure>, <Caption>, <Width linewidth>)
    document.EndSlide()
    ```

4. Compile using
    
    ```python
    document.Compile()
    ```

## Example
Test.py already contains an example of how to use the class. 
In the OutputDirectory, you will find the generated PDF file and also the .tex file.

