powershell.exe -ExecutionPolicy ByPass -noexit -command "& 'C:\ProgramData\anaconda3\shell\condabin\conda-hook.ps1' ; conda activate 'C:\ProgramData\anaconda3'; conda activate MeuAmbiente; cd 'C:\Users\Podengos\Documents\GitHub\rcp-track\src\Camera'; cls; python processImage.py; timeout 3; exit