import subprocess
import openai

def interpret_command(command):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": f"Converta este comando em uma ação Git: {command}"}]
    )
    return response.choices[0].message.content

command = "Faça commit das mudanças no arquivo app.py com a mensagem 'fix: erro de login'"
git_action = interpret_command(command)  # Retorna: "git add app.py && git commit -m 'fix: erro de login'"
subprocess.run(git_action, shell=True)