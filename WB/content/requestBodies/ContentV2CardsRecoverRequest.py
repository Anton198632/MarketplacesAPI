from dataclasses import dataclass


@dataclass
class ContentV2CardsRecoverRequest:
    """
    Восстановление НМ из корзины

    Метод позволяет восстановить НМ из корзины. <span class="newM">new</span><br> <code>ВАЖНО</code>: При восстановлении НМ из корзины она не возвращается в КТ в которой была до переноса в корзину, то есть <code>imtID</code> остается тот же, что и был у НМ в корзине.
    
    """
    #  Артикул WB (max. 1000)
    nmIDs: int
