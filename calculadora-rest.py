#!/usr/bin/python

import webapp
import socket

class miServidor(webapp.webApp):

    def parse(self, request):
        verbhttp = request.split()[0]
        recurso = rec = request.split()[1].split("/")[1]
        cuerpo = request.split()[-1]
        return(verbhttp, recurso, cuerpo)

    def process(self, parsedRequest):
        (verbhttp, recurso, body) = parsedRequest
        result = 0
        if (verbhttp == "PUT"):
            self.operacion = body
            return ("200 OK", "<html><body>Tu operacion es: "
                    + body + "</body></html>")
        elif (verbhttp == "GET"):
            try:
                if (len(self.operacion.split('+')) == 2):
                    result = (float(self.operacion.split("+")[0]) +
                             float(self.operacion.split("+")[1]))
                elif (len(self.operacion.split('-')) == 2):
                    result = (float(self.operacion.split("-")[0]) -
                             float(self.operacion.split("-")[1]))
                elif (len(self.operacion.split('*')) == 2):
                    result = (float(self.operacion.split("*")[0]) *
                             float(self.operacion.split("*")[1]))
                elif (len(self.operacion.split('/')) == 2):
                    result = (float(self.operacion.split("/")[0]) /
                             float(self.operacion.split("/")[1]))
                return ("200 OK",
                        "<html><body>El resultado de la operacion es: " +
                        str(result) + "</body></html>")
            except AttributeError:
                return ("404 Not Found",
                        "<html><body>No hay operacion</body></html>")
            except ValueError:
                return ("404 Not Found",
                        "<html><body>Operacion incorrecta</body></html>")
        else:
            return ("404 Non Found",
                    "<html><body>Operacion incorrecta</body></html>")

if __name__ == "__main__":
    serv = miServidor(socket.gethostname(), 1234)
