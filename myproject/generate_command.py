model="ggml-tiny-q5_1"
cmd = fr".\build\bin\Release\whisper-cli -f myproject\my-1min.wav -l auto -m models\{model}.bin"
print(cmd)