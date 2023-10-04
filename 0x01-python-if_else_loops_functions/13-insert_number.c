#include "lists.h"

/**
 * insert_node - Insert a number into a sorted singly linked list
 * @head: pointer to pointer of first node of listint_t list
 * @number: The number to insert
 *
 * Return: The address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *current = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	if (*head == NULL)
	{
		*head = new;
		return (new);
	}

	while (current->n < number &&
			current->next &&
			current->next->n < number)
		current = current->next;

	if (current->n > number)
	{
		new->next = current;
		*head = new;
	}
	else
	{
		new->next = current->next;
		current->next = new;
	}

	return (new);
}
