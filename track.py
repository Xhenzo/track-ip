import requests
from rich.console import Console
from rich.table import Table
from rich.text import Text
import time

def get_ip_info(ip_address):
    url = f"http://ip-api.com/json/{ip_address}"
    response = requests.get(url)
    data = response.json()
    return data

def display_ip_info(ip_info):
    console = Console()
    
    table = Table(title="Informasi IP", show_header=True, header_style="bold magenta")
    table.add_column("INFORMATION", style="cyan", no_wrap=True)
    table.add_column("RESULT", style="green")
    
    # Menambahkan informasi IP yang lebih lengkap
    fields = [
        "IP", "Status", "Country", "Region", "City", "ZIP", "Latitude", "Longitude",
        "ISP", "Organization", "AS", "Query", "Timezone", "Region Name", "Country Code",
        "Mobile", "Proxy", "Hosting", "Reverse", "City Name", "District", "Metro Code",
        "Area Code", "Dma Code", "Continent", "Currency", "Language", "Timezone Offset",
        "Country Name", "Region Code", "Region Abbreviation", "City Population", "Country Population"
    ]

    for field in fields:
        value = ip_info.get(field.lower(), "N/A")
        table.add_row(field, str(value))

    console.print(table)

def display_logo():
    console = Console()
    logo = Text("""
    ██╗  ██╗    ████████╗██████╗  █████╗  ██████╗██╗  ██╗
    ╚██╗██╔╝    ╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝
     ╚███╔╝        ██║   ██████╔╝███████║██║     █████╔╝ 
     ██╔██╗        ██║   ██╔══██╗██╔══██║██║     ██╔═██╗ 
    ██╔╝ ██╗       ██║   ██║  ██║██║  ██║╚██████╗██║  ██╗
    ╚═╝  ╚═╝       ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
    """, style="bold cyan")

    # Efek kelap-kelip
    for _ in range(1):
        console.print(logo, justify="center")
        time.sleep(0.5)
        console.clear()
        time.sleep(0.5)

    console.print(logo, justify="center")

def main():
    console = Console()
    display_logo()
    console.print(f"[ [bold green]DEVELOPERS[bold white] ] XHENZOSEC\n[ [bold green]GITHUB[bold white] ] https://github.com/Xhenzo")
    ip_address = console.input("[ [bold green]IP TARGET [bold white]] : ")

    try:
        ip_info = get_ip_info(ip_address)
        if ip_info['status'] == 'success':
            display_ip_info(ip_info)
        else:
            console.print("[bold red]FAILED TO GET INFORMATION ON THE IP BECAUSE THE IP IS INCORRECT!![/bold red]")
    except requests.exceptions.RequestException as e:
        console.print(f"[bold red]ERROR : {e}[/bold red]")

if __name__ == "__main__":
    main()
