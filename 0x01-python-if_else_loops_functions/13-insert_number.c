#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
#include <unistd.h>

/**
 * insert_node - function in C that inserts a number
 * into a sorted singly linked list
 * @head: this is a linked list
 * @number: the number to be inserted
 * Return: new head pointer
 *
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head;
	listint_t *new = NULL;
	listint_t *tempo = NULL;

	if (!head)
		return (NULL);
	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (!*head || (*head)->n > number)
	{
		new->next = *head;
		return (*head = new);

	}
	else
	{
		while (current && current->n < number)
		{
			tempo = current;
			current = current->next;
		}
		tempo->next = new;
		new->next = current;
	}
	return (new);
}
