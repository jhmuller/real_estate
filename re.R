library(ggplot2)
library(tidyverse)
library(stargazer)
library(readr)
library(dplyr)
library(magrittr)

df <- readr::read_delim("realtor2.csv", delim="|")

spec(df)

# data minipulations
df$Price <- as.numeric(gsub(",|\\$", '', df$price))
df$SqFt <- as.numeric(gsub(",", '', df$sqft))
df$LotSize <- as.numeric(gsub(",", '', df$lotsize))
df$Beds <- as.numeric(gsub(",", '', df$beds))
df$Baths <- as.numeric(gsub("\\+", '', df$baths))


df$Broker <- df$broker
#df$Broker[grep("otheby",df$broker, ignore.case=TRUE)] <- "Sothebys"
#df$Broker[grep("oldwell",df$broker, ignore.case=TRUE)] <- "Coldwell"
#df$Broker[grep("Raveis",df$broker, ignore.case=TRUE)] <- "Raveis"
#df$Broker[grep("Century",df$broker, ignore.case=TRUE)] <- "Century21"
#df$Broker[grep("Keller",df$broker, ignore.case=TRUE)] <- "Keller"
#df$Broker[grep("Engel",df$broker, ignore.case=TRUE)] <- "Engel"
#df$Broker[grep("re/max",df$broker, ignore.case=TRUE)] <- "ReMax"
#df$Broker[grep("ttias",df$broker, ignore.case=TRUE)] <- "Attias"
#df$Broker[grep("izner",df$broker, ignore.case=TRUE)] <- "izner"
#df$Broker[grep("Bowes",df$broker, ignore.case=TRUE)] <- "Bowes"
#df$Broker[grep("Redfin",df$broker, ignore.case=TRUE)] <- "Redfin"
#df$Broker[grep("Comrie",df$broker, ignore.case=TRUE)] <- "Comrie"
#df$Broker[grep("Pulte",df$broker, ignore.case=TRUE)] <- "Pulte"



x <- group_by(df, Broker) %>% 
  summarise(Cnt = n(), TotValue=sum(Price), MedValue=median(Price)) %>% 
  mutate(AvgValue= TotValue/Cnt) %>%
  arrange(Cnt)
ggplot(x) + geom_point(mapping=aes(x=MedValue, y=Cnt, size=TotValue))


ggplot(x2, mapping=aes(x=Cnt)) + 
  geom_bar(mapping=aes(x=Cnt)) +
  geom_line(mapping=aes(x=Cnt, y=CumCnt)) 

ggplot(x2, mapping=aes(x=TotValue)) + 
  geom_line(mapping=aes(x=TotValue, y=CumValue)) 

      geom_line(mapping=(aes(x=Cnt, y=PctCnt)))
  
  geom_point(mapping=aes(x=Cnt, y=TotValue) )




+ geom_line(aes=mapping(x=Cnt, y=))
+ geom_smooth()


df

df$PriceSqFt <- df$Price / df$SqFt

ggplot(df, mapping=aes(x=Price, y=SqFt, color=town)) + geom_point() + geom_smooth()


ggplot(df) + stat_summary(
  mapping = aes(x = town, y = PriceSqFt),
  fun.ymin = min,
  fun.ymax = max,
  fun.y = median
) + ylim(0, 700)

ggplot(df) + 
  geom_point(mapping=aes(x=town, y=Price), position="jitter")+ ylim(0,3500000) + 
  facet_wrap(~BrokerFac) +
  theme(axis.text.x = element_text(angle = 90, hjust = 1))


ggplot(df) + geom_bar(mapping=aes(x=town, fill=BrokerFac), position="dodge")

ggplot(df) + geom_bar(mapping=aes(x=BrokerFac), position="dodge") + facet_wrap(~town)+
  theme(axis.text.x = element_text(angle = 90, hjust = 1))

+ facet_wrap(~BrokerFac) +
  theme(axis.text.x = element_text(angle = 90, hjust = 1))

ggplot(df) + 
   stat_summary(
  mapping = aes(x = town, y = Price),
  fun.ymin = min,
  fun.ymax = max,
  fun.y = median
)


df <- df[order(df$Price),]

df[df$town =="Concord", c("addres", "SqFt", 'ptype', "LotSize",  "Price")]

