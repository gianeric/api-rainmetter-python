function Initialize()
    ExecutePython()
end

function Update()
    ExecutePython()

    local file = io.open("E:\\Projetos\\api-rainmetter-python\\football\\football.txt", "r")
    if file then
        local trends = file:read("*all")
        file:close()
        return trends
    end

    print("[UPDATE] Erro ao ler os jogos.")
    return "Erro ao ler os jogos"
end

function ExecutePython()
    print("[START] Execute Python")

    local pythonExe = 'E:\\Projetos\\api-rainmetter-python\\env\\Scripts\\python.exe'
    local script = 'E:\\Projetos\\api-rainmetter-python\\football\\football.py'

    --local command = string.format('start /B "" "%s" "%s" > NUL 2>&1', pythonExe, trendsScript)
    local command = string.format('powershell -WindowStyle Hidden -Command "& {Start-Process "%s" "%s" -NoNewWindow}"', pythonExe, script)

    os.execute(command)

    print("[END] Execute Python")
end