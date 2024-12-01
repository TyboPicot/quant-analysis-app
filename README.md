# **Quantitative Analysis Application**

## **I. Description**
Cette application permet de comparer différentes stratégies d'analyse quantitative sur divers produits financiers (actions, devises, matières premières, crypto-monnaies, etc.) afin de fournir des indicateurs pertinents à l'utilisateur. Elle est conçue pour servir de base à un **trading bot**.

L'approche **API First** a été suivie pour ce projet, avec une architecture backend basée sur Flask et un frontend développé en Angular 17 (standalone). Les pratiques **TDD**, **clean code**, **SOLID**, et l'architecture **hexagonale** sont appliquées.

---

## **II. Fonctionnalités**
### Backend :
1. Récupérer la liste des **stratégies d'analyse quantitative** disponibles.
2. Récupérer la liste des **produits financiers** disponibles.
3. Analyser un produit financier en appliquant une **stratégie choisie** sur une plage de données donnée.
4. Vérification de l'état de l'API avec un endpoint **healthcheck**.

---

## **III. Stratégies d'analyse quantitative disponibles**

### 1. Moyennes Mobiles (**Moving Averages**)
- **Type** : Tendance (Trend)
- **Description** : Compare les moyennes mobiles court terme et long terme pour générer des signaux d'achat (BUY) ou de vente (SELL).
- **Sources** :
  - [Documentation sur les moyennes mobiles](https://www.investopedia.com/terms/m/movingaverage.asp)
  - TA-Lib pour calculer les moyennes mobiles.

### 2. Trading par Breakout (**Breakout Trading**)
- **Type** : Tendance (Trend)
- **Description** : Génère des signaux basés sur la sortie des prix d'un canal défini.
- **Sources** :
  - [Stratégie de Breakout sur Investopedia](https://www.investopedia.com/terms/b/breakout.asp)

### 3. Retour à la Moyenne (**Mean Reversion**)
- **Type** : Contrarian
- **Description** : Identifie les moments où les prix s'éloignent trop de leur moyenne historique et parient sur un retour à cette moyenne.
- **Sources** :
  - [Concept de Mean Reversion](https://www.investopedia.com/terms/m/meanreversion.asp)

### 4. Divergence RSI (**RSI Divergence**)
- **Type** : Momentum
- **Description** : Analyse les divergences entre le prix et l'indicateur RSI pour détecter des inversions de tendance.
- **Sources** :
  - [Guide complet sur le RSI](https://www.investopedia.com/terms/r/rsi.asp)

### 5. Pair Trading (**Pair Trading**)
- **Type** : Statistique
- **Description** : Analyse la corrélation entre deux actifs similaires et exploite les écarts statistiques entre eux.
- **Sources** :
  - [Introduction au Pair Trading](https://www.investopedia.com/terms/p/pairs_trade.asp)

---

## **IV. Produits financiers disponibles**
Liste initiale des produits financiers disponibles (exemple) :
- **Actions (stocks)** :
  - Apple Inc. (**AAPL**)
  - Alphabet Inc. (**GOOGL**)
- **Devises (currency)** :
  - Euro / Dollar américain (**EURUSD**)
- **Matières premières (commodities)** :
  - Or (**XAUUSD**)
- **Crypto-monnaies (cryptocurrency)** :
  - Bitcoin (**BTCUSD**)

---

## **V. Structure du projet**

### **Arborescence du Backend**
```plaintext
backend/
├── app/
│   ├── controllers/
│   │   ├── __init__.py
│   │   ├── strategies.py
│   │   └── products.py
│   ├── services/
│   │   ├── __init__.py
│   │   └── analysis_service.py
│   ├── models/
│   │   └── __init__.py
│   ├── repositories/
│   │   └── __init__.py
│   ├── utils/
│   │   └── __init__.py
│   ├── __init__.py
│   ├── config.py
├── tests/
│   ├── __init__.py
│   ├── test_healthcheck.py
│   ├── test_products.py
├── main.py
├── requirements.txt
└── README.md
```

## **VI. Endpoints de l'API**

### **1. Healthcheck**
- **Description** : Vérifie si l'API est opérationnelle.
- **Méthode** : `GET`
- **URL** : `/healthcheck`
- **Réponse** :
  ```json
  {
    "status": "OK"
  }
  ```

### **2. Liste des stratégies**

- **Description** : Récupère la liste des stratégies d'analyse disponibles.
- **Méthode** : `GET`
- **URL** : `/strategies`
- **Réponse** :
  ```json
    {
        "strategies": 
        [
            {"id": "moving_average", "name": "Moving Averages", "type": "trend"},
            {"id": "breakout", "name": "Breakout Trading", "type": "trend"},
            {"id": "mean_reversion", "name": "Mean Reversion", "type": "contrarian"},
            {"id": "rsi_divergence", "name": "RSI Divergence", "type": "momentum"},
            {"id": "pair_trading", "name": "Pair Trading", "type": "statistical"}
        ]
    }
  ```

### **3. Liste des produits financiers**

- **Description** : Récupère la liste des produits financiers disponibles.
- **Méthode** : `GET`
- **URL** : `/products`
- **Réponse** :
  ```json
    {
        "products": 
        [
            {"symbol": "AAPL", "name": "Apple Inc.", "category": "stock"},
            {"symbol": "GOOGL", "name": "Alphabet Inc.", "category": "stock"},
            {"symbol": "EURUSD", "name": "Euro / US Dollar", "category": "currency"},
            {"symbol": "XAUUSD", "name": "Gold", "category": "commodity"},
            {"symbol": "BTCUSD", "name": "Bitcoin", "category": "cryptocurrency"}
        ]
    }
  ```

### **4. Analyse quantitative**

- **Description** : Lance une analyse sur un produit financier avec une stratégie choisie.
- **Méthode** : `POST`
- **URL** : `/analyse`
- **Payload** :
  ```json
    {
        "ticker": "AAPL",
        "strategy": "moving_average",
        "start_date": "2023-01-01",
        "end_date": "2023-12-31"
    }
  ```
- **Réponse** :
  ```json
    {
        "signals": 
        [
            {"date": "2023-05-01", "signal": "BUY"},
            {"date": "2023-07-15", "signal": "SELL"}
        ],
        "cumulative_return": 12.34,
        "max_drawdown": -5.67,
        "sharpe_ratio": 1.45
    }
  ```

## **VII. Installation et utilisation**
### **1. Backend**
Clonez le projet :
```bash
git clone <repository-url>
cd backend
```
Installez les dépendances :
```bash
pip install -r requirements.txt
```
Lancez l'application :
```bash
python main.py
```
L'API sera disponible sur http://localhost:5000.
### **2. Tests**
Pour exécuter les tests, utilisez :

```bash
pytest tests/
```
