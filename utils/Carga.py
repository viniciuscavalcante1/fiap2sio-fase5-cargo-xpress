import random


class Carga:
    def __init__(self, horario_fila_de_carga: str = None, horario_carregada: str = None):
        lista_roupas = [
            "Camisa Xadrez",
            "Calça Jeans Skinny",
            "Jaqueta de Couro Vintage",
            "Saída de Praia Estampada",
            "Sutiã de Amamentação Confortável",
            "Cueca Boxer de Algodão",
            "Pijama Listrado de Flanela",
            "Luva de Frio Acolchoada",
            "Vestido Floral Midi",
            "Camisa Social Branca",
            "Bermuda Cargo Camuflada",
            "Blusa de Tricô Grande",
            "Calça Legging Esportiva",
            "Terno Clássico Preto",
            "Macacão Jeans Elegante",
            "Chapéu de Palha para Praia",
            "Tênis de Corrida Leve",
            "Vestido de Festa Longo",
            "Camisa Estampada Tropical",
            "Shorts de Praia Colorido",
            "Blazer de Linho Casual",
            "Camisola de Seda",
            "Meia-calça Opaca",
            "Camiseta Básica de Algodão",
            "Calça Chino Slim",
            "Jaqueta Corta-vento",
            "Biquíni de Cintura Alta",
            "Gravata de Seda",
            "Moletom com Capuz",
            "Vestido Tubinho Preto",
            "Camisa Polo Listrada",
            "Calça de Moletom Confortável",
            "Top Esportivo de Compressão",
            "Vestido de Noiva Elegante",
            "Camisa Jeans Despojada",
            "Legging Estampada",
            "Blusa Ombro a Ombro",
            "Paletó de Veludo",
            "Short Saia de Cintura Alta",
            "Suéter de Lã Quente",
            "Vestido Longo Estampado",
            "Camiseta Vintage Retrô",
            "Calça Cargo Utilitária",
            "Jaqueta Corta-vento",
            "Maiô de Uma Peça",
            "Gravata Borboleta",
            "Moletom com Estampa",
            "Vestido de Cocktail Sofisticado",
            "Camisa Estampada Artsy",
            "Calça Jogger Casual",
            "Blusa de Alça Fina",
            "Blazer de Lã",
            "Macaquinho Estampado",
            "Calça Flare Elegante",
            "Jaqueta Jeans Clássica",
            "Biquíni de Estilo Retrô",
            "Cachecol de Lã",
            "Conjunto Esportivo Matching",
            "Vestido Solto de Verão",
            "Camisa de Linho Leve",
            "Calça Cargo com Bolsos",
            "Jaqueta Bomber Estilosa",
            "Maiô de Corte Alto",
            "Gravata Estampada",
            "Moletom com Design Exclusivo",
            "Vestido de Noite Deslumbrante",
            "Camiseta Estampada Statement",
            "Legging de Cintura Alta",
            "Blusa de Manga Sino",
            "Blazer Xadrez Elegante",
            "Short Saia Estampado",
            "Suéter de Gola Alta",
            "Vestido Midi Elegante",
            "Camiseta com Frase Inspiradora",
            "Calça Culotte Moderna",
            "Jaqueta de Veludo",
            "Maiô Asa-delta",
            "Gravata Slim",
            "Moletom com Capuz de Zíper",
            "Vestido de Coquetel Elegante",
            "Calça de Alfaiataria",
            "Conjunto de Lingerie Rendado",
            "Cachecol Estampado",
            "Shorts Esportivos Confortáveis",
            "Vestido Envelope Estilizado",
            "Camiseta Listrada Náutica",
            "Calça de Yoga Flexível",
            "Jaqueta Puffer Acolchoada",
            "Maiô Asa-delta",
            "Gravata Slim",
            "Moletom com Estampa Gráfica",
            "Vestido de Coquetel Elegante",
            "Camisa Estampada Étnica",
            "Calça de Alfaiataria",
            "Jaqueta de Ganga Desgastada",
            "Conjunto de Lingerie Rendado",
            "Cachecol Estampado",
            "Shorts Esportivos Confortáveis",
            "Camiseta Listrada Náutica",
            "Calça de Yoga Flexível",
            "Jaqueta Puffer Acolchoada",
            "Top Esportivo de Alta Sustentação",
            "Boné de Beisebol",
            "Vestido de Veludo Vintage",
            "Camisa Social Listrada",
            "Calça Culotte Estampada",
            "Jaqueta de Couro Clássica",
            "Top Cropped",
            "Cinto de Couro Trançado",
            "Saia Jeans Desfiada",
            "Vestido de Verão Estampado",
            "Camiseta Estampada Abstrata",
            "Calça Jogger de Algodão",
            "Jaqueta Jeans com Patches",
            "Sutiã Esportivo de Alta Sustentação",
            "Bandana Estampada",
            "Saia Midi Plissada",
            "Vestido Estampado de Folhagem",
            "Camiseta Estampada com Arte",
            "Calça de Alfaiataria Cropped",
            "Jaqueta Jeans Grande",
            "Sutiã de Renda Delicado",
            "Bandana de Seda",
            "Saia de Couro",
            "Vestido de Verão Estampado",
            "Camisa Jeans Despojada",
            "Legging Estampada",
            "Blusa Ombro a Ombro",
            "Paletó de Veludo",
            "Short Saia de Cintura Alta",
            "Suéter de Lã Quente",
            "Vestido Longo Estampado",
            "Camiseta Vintage Retrô",
            "Calça Cargo Utilitária",
            "Jaqueta Corta-vento",
            "Maiô de Uma Peça",
            "Gravata Borboleta"]
        self.id_carga = random.randint(0, 999)
        self.nome_produto = random.choice(lista_roupas)
        self.horario_fila_de_carga = horario_fila_de_carga
        self.horario_carregada = horario_carregada

    def __str__(self):
        return str(f"{self.nome_produto} - ID: {self.id_carga}")

    def set_horario_fila_de_carga(self, horario_fila_de_carga: str):
        self.horario_fila_de_carga = horario_fila_de_carga

    def set_horario_carregada(self, horario_carregada: str):
        self.horario_carregada = horario_carregada

    def get_horario_fila_de_carga(self):
        return self.horario_fila_de_carga

    def get_horario_carregada(self):
        return self.horario_carregada

    def get_tempo_de_espera(self):
        return (int(self.get_horario_carregada().replace("20h", ""))
                - int(self.get_horario_fila_de_carga().replace("20h", "")))
