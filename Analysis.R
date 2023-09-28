install.packages(tidyverse)

library(tidyverse)

tb = read_csv("data/evaluation.csv")

arrange(tb, tb$`open-meteo-elevation`)
cor.test(tb$`open-meteo-elevation`, tb$`mapillary-altitude`)
ggplot(tb, aes(`mapillary-altitude`, `open-meteo-elevation`, )) + geom_point() + labs(y="Elevation data from Open Meteo", x="Altitude data extracted from Mapillary Sequences") + geom_smooth(method="lm")
#  90 meters resolution

model <- lm(tb$`open-meteo-elevation` ~ tb$`mapillary-altitude`)
summary(model)

mean(tb$`mapillary-altitude`)
mean(tb$`open-meteo-elevation`)
mean(tb$`open-meteo-elevation`) - mean(tb$`mapillary-altitude`)

cor(tb$`open-meteo-elevation` ,tb$`mapillary-altitude`)

boxplot(tb$`mapillary-altitude`~tb$`open-meteo-elevation`)
