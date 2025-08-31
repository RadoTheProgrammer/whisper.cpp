
* go to dir models to download
* command for windows to download `models\download-ggml-model.cmd <model>`

command to build with SDL2: 
cmake -B build -DCMAKE_PREFIX_PATH="C:\Users\rrrad\OneDrive - Education Vaud\Documents\coding\vcpkg\installed\x64-windows" -DWHISPER_SDL2=ON

command to transcript:
```
.\build\bin\Release\whisper-cli -f myproject\my-1min.wav -l auto -m models\<model>.bin > myproject\transcriptions\<model>.txt
```