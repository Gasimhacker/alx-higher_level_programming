#include "lists.h"

/**
 * check_cycle - Check if a singly linked list has a cycle in it
 * @list: A pointer to the head of the list
 *
 * Return: If there is no cycle - 0
 *	   if there is a cycle - 1
 */
int check_cycle(listint_t *list)
{
	listint_t *tortoise = list;
	listint_t *hare = NULL;

	if (list == NULL)
		return (0);

	if (list && list->next)
		hare = list->next->next;

	while (tortoise != hare && hare)
	{
		tortoise = tortoise->next;
		if (hare && hare->next)
			hare = hare->next->next;
		else
			return (0);
	}
	if (tortoise != hare)
		return (0);

	return (1);
}
