#-*- coding:utf-8 -*-
import networkx as nx
from trabalho_1.bl import BancoLogico

from inspect import isroutine

class ArvoreBidirecional:

    def __init__(self):
        self.g = nx.DiGraph()
        self.bl = BancoLogico()

        self.montar_arvore()

    def determinar_parametros_teste(self):
        self.bl.quantia_poupada(30000)
        self.bl.ganhos(27000, self.bl.ESTAVEL)
        self.bl.dependentes(3)

    def montar_arvore(self):
        self.g.add_path((self.bl,
                          self.bl.poupanca_inadequada,
                          self.bl.investimento_poupanca,
                          self.bl.investimento_seguro
                         ))
        self.g.add_path((self.bl,
                          self.bl.poupanca_adequada,
                          self.bl.renda_adequada,
                          self.bl.investimento_acoes,
                          self.bl.investimento_seguro
                         ))

        self.g.add_path((self.bl,
                          self.bl.poupanca_adequada,
                          self.bl.renda_inadequada,
                          self.bl.investimento_ambos,
                          self.bl.investimento_seguro
                         ))

    def buscar_investimento_seguro(self):
        """Um investimento seguro só é possível se todos nós, do pai ao filho,
        são validados como verdadeiros no caminho correspondente. O próprio
        caminho diz qual investimento seguir."""
        buscador_do_inicio = Buscador(graph=self.g,
                                      no_inicial=self.bl,
                                      objetivo=self.bl.investimento_seguro,
                                      funcao_proximo_no=self.g.successors)
        #buscador "espelho" do buscador_do_inicio
        buscador_do_fim    = Buscador(graph = buscador_do_inicio.graph,
                                      no_inicial = buscador_do_inicio.objetivo,
                                      objetivo = buscador_do_inicio.no_atual, #nó inicial
                                      funcao_proximo_no=self.g.predecessors)

        buscadores = [None, buscador_do_inicio, buscador_do_fim]
        flag = 1

        while not (buscador_do_inicio.esbarrou(buscador_do_fim) or \
                    buscador_do_inicio.atingiu_objetivo() or \
                    buscador_do_fim.esbarrou(buscador_do_inicio) or \
                    buscador_do_fim.atingiu_objetivo()):
            #flag para fazer apenas um buscador caminhar a cada passo ("loop")
            buscadores[flag].step()
            flag *= -1

        self.mostrar_resultados(buscador_do_inicio, buscador_do_fim)

    def mostrar_resultados(self, buscador_do_inicio, buscador_do_fim):
        print "Caminhos: "
        print "Buscador do início: " + str(buscador_do_inicio.path)
        print "Buscador do fim: " + str(buscador_do_fim.path)
        print "Nó no buscador do início: " + str(buscador_do_inicio.no_atual)
        print "Nó no buscador do fim: " + str(buscador_do_fim.no_atual)


class Buscador:
    def __init__(self, graph, no_inicial, objetivo, funcao_proximo_no):
        self.graph = graph
        self.no_atual = no_inicial
        self.objetivo = objetivo
        self.funcao_proximo_no = funcao_proximo_no
        self.path = [self.no_atual,]
        self.validar_no()

    def validar_no(self):
        self.graph[self.no_atual].setdefault('visitado_por', [])
        self.graph[self.no_atual]['visitado_por'].append(self)
        self.graph[self.no_atual]['validado_como'] = self.no_atual()

    def esbarrou(self, outro_buscador):
        """Só irá realmente esbarrar caso se encontre com o outro buscador
        num nó validado como verdadeiro, pois o self.no_atual só recebe o nó
        atualmente a ser verificado se este:
            - não tiver sido visitado
            ou
            - tiver sido visitado, porém estar validado como verdadeiro
        """
        return self.no_atual == outro_buscador.no_atual

    def atingiu_objetivo(self):
        self.no_atual == self.objetivo

    def step(self):
        #se nó atual está validado como False, busca outra rota
        if self.graph[self.no_atual]['validado_como'] == False:
            self.path.pop()
            self.no_atual = self.path[-1]
            return self.step()

        proximo_no = None
        for no in self.funcao_proximo_no(self.no_atual):
            if isroutine(no):
                #no é função e ainda não é visitado
                if not self.graph[no].has_key('validado_como') or \
                    (self.graph[no]['validado_como'] == True and not self in \
                        self.graph[no]['visitado_por']): #nó validado como verdadeiro, mas ainda não visitado
                    proximo_no = no
                    break
        if proximo_no: #encontrou um próximo nó válido
            self.no_atual = proximo_no
            self.path.append(proximo_no)
            self.validar_no()
            return

        if not proximo_no: #não encontrou um próximo nó válido
            self.path.pop()
            self.no_atual = self.path[-1]
            return self.step()

