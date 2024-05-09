Sub MergeDataByMatchingColumns()

Dim wsOutstanding As Worksheet, wsPortfolio As Worksheet, wsMerged As Worksheet
Dim dataOutstanding As Variant, dataPortfolio As Variant
Dim matchCol11 As Long, matchCol12 As Long, matchCol21 As Long, matchCol22 As Long
Dim lastRow1 As Long, lastRow2 As Long
Dim i As Long, j As Long, k As Long

' Define worksheets
Set wsOutstanding = ThisWorkbook.Worksheets("OutstandingReport")
Set wsPortfolio = ThisWorkbook.Worksheets("portfolioDataLive")

' Define matching columns (1-based index)
' In OutstandingReport
matchCol11 = wsOutstanding.Cells(1, Columns.Count).End(xlToLeft).Column ' Last column containing data (ELN No)
matchCol12 = 1 ' Assuming UL Name is in the first column

' In portfolioDataLive
matchCol21 = wsPortfolio.Cells(1, Columns.Count).End(xlToLeft).Column ' Last column containing data (CC Underlying Name)
matchCol22 = 3 ' Assuming CC ELN No is in the third column (adjust based on your actual data)

' Get data from worksheets
lastRow1 = wsOutstanding.Cells(Rows.Count, 1).End(xlUp).Row
lastRow2 = wsPortfolio.Cells(Rows.Count, 1).End(xlUp).Row
dataOutstanding = wsOutstanding.Range(wsOutstanding.Cells(2, 1), wsOutstanding.Cells(lastRow1, matchCol11)).Value  ' Capture relevant columns from OutstandingReport
dataPortfolio = wsPortfolio.Range(wsPortfolio.Cells(2, 1), wsPortfolio.Cells(lastRow2, matchCol21)).Value  ' Capture relevant columns from portfolioDataLive

' Find matching rows
Dim mergedData As Variant
ReDim mergedData(1 To UBound(dataOutstanding, 1) + UBound(dataPortfolio, 1), UBound(dataOutstanding, 2) + UBound(dataPortfolio, 2))

k = 1
For i = 1 To UBound(dataOutstanding, 1)
    For j = 1 To UBound(dataPortfolio, 1)
        If dataOutstanding(i, matchCol11) = dataPortfolio(j, matchCol22) And dataOutstanding(i, matchCol12) = dataPortfolio(j, matchCol21) Then  ' Check for both ELN No and UL Name match
            For m = 1 To UBound(dataOutstanding, 2)
                mergedData(k, m) = dataOutstanding(i, m)
            Next m
            For m = UBound(dataOutstanding, 2) + 1 To UBound(dataPortfolio, 2)
                mergedData(k, m) = dataPortfolio(j, m)
            Next m
            k = k + 1
            Exit For ' Exit inner loop after finding a match
        End If
    Next j
Next i

' Create new worksheet for merged data
Set wsMerged = ThisWorkbook.Worksheets.Add
wsMerged.Name = "Merged Table"  ' Set the name of the new worksheet

' Write merged data to the new worksheet
wsMerged.Range("A1").Resize(UBound(mergedData, 1), UBound(mergedData, 2)).Value = mergedData

End Sub
