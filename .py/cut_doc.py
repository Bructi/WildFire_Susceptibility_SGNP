import win32com.client
import os
import sys

doc_path = os.path.abspath(r"d:\Aniket\majja\Project_Report_v4.docx")
out_path = os.path.abspath(r"d:\Aniket\majja\Project_Report_v4_30pages.docx")

try:
    word = win32com.client.DispatchEx("Word.Application")
    word.Visible = False
    
    doc = word.Documents.Open(doc_path)
    
    pages = doc.ComputeStatistics(2) # wdStatisticPages = 2
    print(f"Original pages: {pages}")
    
    if pages > 30:
        # Move start of range to page 31
        # wdGoToPage = 1, wdGoToAbsolute = 1
        rng = doc.Range(0, 0)
        rng.SetRange(Start=doc.Content.Start, End=doc.Content.End)
        
        # Word's Selection object might be easier, but let's try Range
        # To get the start position of page 31:
        # wdGoToPage = 1, wdGoToAbsolute = 1
        page_31_range = doc.GoTo(1, 1, 31)
        
        delete_range = doc.Range(page_31_range.Start, doc.Content.End)
        delete_range.Delete()
        
        doc.SaveAs(out_path)
        print(f"Successfully cut the document. Saved to: {out_path}")
    else:
        print("Document is already 30 pages or less.")
    
    doc.Close(False)
    word.Quit()
except Exception as e:
    print(f"Error: {e}")
    try:
        word.Quit()
    except:
        pass
    sys.exit(1)
