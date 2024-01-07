#include "lists.h"
#include <stdio.h>

void reverse(listint_t **head);
int compare_lists(listint_t *head, listint_t *middle, int len);


/**
 * is_palindrome - this function checks
 *  if a singly linked list is a palindrome
 *
 * @head: the pointer to the ponter 
 * of the first node in passed list
 *
 * Return: 0 if palidrome is not detected, 1 if detected
 */
int is_palindrome(listint_t **head)
{
	int len, j;
	listint_t *temp;
	listint_t *middle;

	if (head == NULL || *head == NULL)
		return (1);
	temp = *head;
	middle = *head;

	for (len = 0; temp != NULL; len++)
		temp = temp->next;

	len = len / 2;

	for (j = 1; j < len; j++)
		middle = middle->next;
	if (len % 2 != 0 && len != 1)
	{
		middle = middle->next;
		len = len - 1;
	}
	reverse(&middle);
	j = compare_lists(*head, middle, len);

	return (j);
}

/**
 * compare_lists - compares the two lists
 * @head: the pointer to the head node
 * @middle: pointer to the middle node
 * @len: the length of the list
 *
 * Return: 1 if it is the same, 0 if not
 */
int compare_lists(listint_t *head, listint_t *middle, int len)
{
	int j;

	if (head == NULL || middle == NULL)
		return (1);
	for (j = 0; j < len; j++)
	{
		if (head->n != middle->n)
			return (0);
		head = head->next;
		middle = middle->next;

	}
	return (1);
}

/**
 * reverse - reverses a list
 * @head: the pointer to the head to reverse
 */
void reverse(listint_t **head)
{
	listint_t *current;
	listint_t *next;
	listint_t *prev;

	if (head == NULL || *head == NULL)
		return;

	prev = NULL;
	current = *head;
	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	*head = prev;
}
