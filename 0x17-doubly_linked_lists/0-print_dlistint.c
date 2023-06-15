#ifndef LISTS_H
#define LISTS_H


/* Structure for doubly linked list */
typedef struct dlistint_s
{
    int n;
    struct dlistint_s *prev;
    struct dlistint_s *next;
} dlistint_t;
 
#endif /* LISTS_H */
