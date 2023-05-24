import openai   
import config
import typer
from rich import print
from rich.table import Table

def main(): 
    
    openai.api_key = config.api_key
    
    print("💬 [bold green]Bienvenido al asistente de OpenAI[/bold green]")
    
    table = Table("comandos", "descripcion")
    table.add_row("exit", "Salir del asistente")
    table.add_row("new", "Crear un nuevo archivo")
    
    print(table)
   
    
    #contexto del asistente
    context = {"role": "system", 
             "content": "Eres un asistente muy util."}
    mensajes = [context]

    while True:
        
        content = __prompt()
        
        if content == "new":
            print("🆕 ¡Nueva conversacion!")
            mensajes= [context]
            content = __prompt()
            
        mensajes.append({"role": "user", "content": content})

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", mensajes=mensajes)
        
        response_content = response.choices[0].message.content
        
        mensajes.append({"role": "assistant", "content": response_content})
                                
        print(f"[bold green]> [/bold green] [green]{response_content}[/green]")
        
        
def __prompt() -> str:
        prompt = typer.prompt("\nSobre que quieres hablar? ")
        
        if prompt == "exit":
            exit = typer.confirm("⚠️ Estas seguro?")
            if exit:
                print("👋 Hasta luego!")
                raise typer.Abort()  
            return __prompt()      
        return prompt
            
    
if __name__ == "__main__":
    typer.run(main)