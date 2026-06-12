# TOPSIS - Technique for Order of Preference by Similarity to Ideal Solution

## 📋 Description

Ce projet implémente la **méthode TOPSIS**, un algorithme d'aide à la décision multicritère qui classe les alternatives selon leur similarité avec la solution idéale positive et leur distance de la solution idéale négative.

Le projet se concentre sur l'application du TOPSIS à la **sélection optimale de matériaux composites FGM (Functionally Graded Materials)** - des matériaux à gradient fonctionnel combinant des propriétés de céramique et de métal.

## 🎯 Fonctionnalités principales

### 1. **Algorithme TOPSIS** (`optimization/topsis.py`)
- Classement multi-critères des alternatives
- Support des critères de bénéfice et de coût
- Calcul des scores normalisés (0-1)
- Génération automatique de classements

### 2. **Propriétés des Matériaux FGM** (`fgm/material_properties.py`)
- Calcul des propriétés élastiques (Module d'Young E, coefficient de Poisson ν)
- Calcul de la densité à travers l'épaisseur
- Calcul des fréquences non-dimensionnelles
- Support de plusieurs matériaux :
  - **Céramiques** : Al₂O₃, ZrO₂, Si₃N₄
  - **Métaux** : Al, Ti-6Al-4V, SUS304

### 3. **Tests et Validation** (`tests/test_topsis.py`)
- Tests unitaires pour valider les scores TOPSIS
- Validation des critères de coût et bénéfice
- Tests des propriétés FGM

### 4. **Réseaux de Neurones** (`ann/`)
- Framework pour la prédiction des propriétés (en développement)

## 📦 Installation

### Prérequis
- Python 3.8+

### Installation des dépendances

```bash
pip install -r requirements.txt
