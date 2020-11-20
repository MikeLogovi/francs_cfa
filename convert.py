def simple_to_letter(number):
    dico={
        1:'un',2:'deux',3:'trois',4:'quatre',5:'cinq',6:'six',7:'sept',8:'huit',9:'neuf',
        10:'dix',11:'onze',12:'douze',13:'treize',14:'quatorze',15:'quinze',16:'seize',
        20:'vingt',30:'trente',40:'quarante',50:'cinquante',60:'soixante',80:'quatre-vingt',
    }
    return dico[number]
def convert_less_or_equal_thousand(number):
    if(number<=16):
        return simple_to_letter(number)
    if(16<number and number<20):
        return simple_to_letter(10)+"-"+simple_to_letter(number%10)
    if((20<=number and number<70) or(80<=number and number<90)):
        return simple_to_letter(number) if number%10 == 0 else simple_to_letter((number//10)*10)+" et "+simple_to_letter(number%10)
    if((70<=number and number<80) or (90<=number and number<100)):
        return simple_to_letter(number) if(number%10==0) else simple_to_letter((number//10)*10-10)+" "+convert_less_or_equal_thousand(number-((number//10)*10-10))    
    if(100<=number and number<1000):
        if(number%100==0):
            return "cent" if number==100 else  convert_less_or_equal_thousand(number//100)+' cents'
        else:
            if((number//100)==1):
                return simple_to_letter(100)+" "+convert_less_or_equal_thousand(number-100)
            else:
                return simple_to_letter((number//100))+" cents "+convert_less_or_equal_thousand(number%100)    
def conversion(number):
    frs_cfa='francs CFA'
    res=""
    milliard,reste=number//1000000000,number%1000000000
    if milliard!=0:
        res= convert_less_or_equal_thousand(milliard) + (" milliard" if milliard==1 else " milliards")
    million,reste=reste//1000000,reste%1000000
    if million!=0:
        res= res + " "+convert_less_or_equal_thousand(million) + (" million" if million==1 else " millions")
    mille,reste=reste//1000,reste%1000
    if mille!=0:
        if mille==1:
            res=res+" mille"
        else:
            res= res + " "+convert_less_or_equal_thousand(mille) + " mille"
    if(reste!=0):
        res = res+" "+convert_less_or_equal_thousand(reste)
    return res+ " "+ frs_cfa

