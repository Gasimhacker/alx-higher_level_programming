#ifndef LISTS_H
#define LISTS_H

#include <stdio.h>
#include <stdlib.h>


/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 * for project
 */
typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

/**
 * print_listint - prints all elements of a listint_t list
 * @h: pointer to head of list
 * Return: number of nodes
 */
size_t print_listint(const listint_t *h);

/**
 * add_nodeint_end - adds a new node at the end of a listint_t list
 * @head: pointer to pointer of first node of listint_t list
 * @n: integer to be included in new node
 * Return: address of the new element or NULL if it fails
 */
listint_t *add_nodeint_end(listint_t **head, const int n);

/**
 * free_listint - frees a listint_t list
 * @head: pointer to list to be freed
 * Return: void
 */
void free_listint(listint_t *head);

/**
 * is_palindrome - Check if a singly linked list is a palindrome
 * @head: pointer to pointer of first node of listint_t list
 *
 * Return: If it is palindorme(An empty list is considered a palindrome) - 1
 *	   otherwise - 0
 */
int is_palindrome(listint_t **head);

#endif /* LISTS_H */
