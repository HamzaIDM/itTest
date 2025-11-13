#include <stdio.h>
#include <stdlib.h>

/*
EXO 1: typedef struct
{
    float reel;
    float img;
}COMPLEXE;

COMPLEXE* AllocationTab(int taille)
{
    COMPLEXE *T;
    T =  (COMPLEXE*)malloc(sizeof(COMPLEXE));
    if(T == NULL)
    {
        printf("Erreur: Probleme d'allocation de la memoire!\n");
        exit(1);
    }
    return T;
}
COMPLEXE** AllocationTab(int N , int M)
{
    COMPLEXE** Mat;
    int i;

    Mat = (COMPLEXE**)malloc(N*sizeof(COMPLEXE*));
    if(Mat == NULL)
    {
        printf("Erreur: Probleme d'allocation de la memoire!\n");
        exit(1);
    }

    for (i = 0; i < N; i++)
    {
        Mat[i] = (COMPLEXE*)malloc(M*sizeof(COMPLEXE));
        if(Mat[i] == NULL)
        {
            printf("Erreur: Probleme d'allocation de la memoire!\n");
            exit(1);
        }
    }

    return Mat;
}*/

typedef struct
{
    int taille;
    int lmax;
    float *tab;
}LISTE;

void creeListe(LISTE *liste , int lmax)
{
    liste->taille = 0;
    liste->lmax = lmax;
    liste->tab = (float*)malloc(lmax*sizeof(float));
}

void insererDebut(LISTE *liste , float value)
{
    if(liste->taille == 0)
    {
        liste->tab[0] = value;
        return;
    }

    int i;
    if(liste->taille == liste->lmax)
    {
        (liste->lmax) += 10 ;
        liste->tab = (float*)realloc(liste->tab,liste->lmax);
    }
    for (i = liste->taille; i > 0; i--)
    {
        liste->tab[i] = liste->tab[i-1];
        liste->tab[0] = value;
    }
    (liste->tab)++;
}
void afficher(LISTE *liste)
{
    int i;
    printf("Taille Maixmale: %d\n",liste->lmax);
    printf("Taille reel: %d\n",liste->taille);
    printf("Les elements du tableau: ");
    for (i = 0; i < liste->taille; i++)
        printf("%.2f  ",liste->tab[i]);
}

void detruireListe(LISTE *liste)
{
    free(liste->tab);
    liste->tab = NULL;
    liste->lmax = liste->taille = 0;
}
void supprimerEltListePos(LISTE *liste , int pos)
{
    if(pos < 0 || pos > liste->taille)
    {
        printf("Position invalide!!\n");
        return;
    }
    int i;
    for (i = pos; i < (liste->taille)-1; i++)
        liste->tab[i] = liste->tab[i+1];

    (liste->tab)--;
}
void supprimerOccurance(LISTE *liste , float value)
{
    int i;
    for (i = 0; i < liste->taille; i++)
        if(liste->tab[i] == value)
            supprimerEltListePos(liste,i--);
}

LISTE* clonerListe(LISTE *liste)
{
    LISTE copy;
    copy.lmax = liste->lmax;
    copy.taille = liste->taille;

    for (int i = 0; i < liste->taille; i++)
        copy.tab[i] = liste->tab[i];
    return &copy;
}
int main()
{
    LISTE L;
    LISTE* pL = (LISTE*)malloc(sizeof(LISTE));

    creeListe(&L , 5);
    creeListe(pL , 5);

    insererDebut(&L , 5.5);
    insererDebut(pL , 1.3);


    system("pause");
    return 0;
}