#include "lists.h"

/**
 * check_cycle - this function checks if a singly linked list has a cycle in it
 * @list: the linked list
 * Return: 1 if cycle exixts and 0 if it does not
 */

int check_cycle(listint_t *list)
{
	listint_t *fast, *slow;

	if (!list || !list->next)
		return (0);
	fast = list;
	slow = list;

	while (slow != NULL && fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
		{
			return (1);
		}
	}
	return (0);
}
