function Initialize()
    ExecutePython()
end

function Update()
    ExecutePython()

    local file = io.open("E:\\Projetos\\api-rainmetter-python\\trends\\trends.txt", "r")
    if file then
        local trends = file:read("*all")
        file:close()
        return trends
    end

    print("[UPDATE] Erro ao ler as tendencias.")
    return "Erro ao ler as tendencias"
end

function ExecutePython()
    print("[START] Execute Python")

    local pythonExe = 'E:\\Projetos\\api-rainmetter-python\\env\\Scripts\\python.exe'
    local trendsScript = 'E:\\Projetos\\api-rainmetter-python\\trends\\trends.py'

    local command = string.format('start /B "" "%s" "%s" > NUL 2>&1', pythonExe, trendsScript)
    os.execute(command)

    print("[END] Execute Python")
end