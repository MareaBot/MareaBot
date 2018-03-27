# coding=utf-8
from mareabot.firebase_db import FirebaseDB

RED_CIRCLE = "🔴"
GRAY_CIRCLE = "🔘"
UP = "🔺"
DOWN = "🔻"
TIMEWATCH = "⌚"
CALENDAR = "📆"


class Previsione():
    def __init__(self, previsione, estremale, tipo, valore):
        self.data_previsione = previsione
        self.data_estremale = estremale
        self.date, self.time = self.data_estremale.split(" ")
        self.tipo = tipo
        self.valore = valore

    def min_max(self):
        text = ""
        if self.tipo == "min":
            text += DOWN
        else:
            text += UP
        text += str(self.valore)
        return text

    def hour(self):
        return TIMEWATCH + str(self.time)

    def calendar(self):
        return CALENDAR + str(self.date)

    def long_string(self):
        return self.calendar() + self.hour() + self.min_max() + "\n"

    def __str__(self):
        return self.long_string()


class DBIstance:
    def __init__(self):
        self.firebase_istance = FirebaseDB().db
        self.prevision = []

    @property
    def last(self):
        return self.last.get()

    @last.getter
    def last(self):
        return self.firebase_istance.child("prevision").child("last").get().val()

    @last.setter
    def last(self, last):
        self.firebase_istance.child("prevision").set({"last": str(last)})

    @property
    def message(self):
        return self.message.get()

    @message.getter
    def message(self):
        return self.firebase_istance.child("message").child("last").get().val()

    @message.setter
    def message(self, message):
        self.firebase_istance.child("message").set({"last": str(message)})