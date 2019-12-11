#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - Function that inserts a number into sorted singly linked list
 * @head: Pointer to pointer type listint_t
 * @number: Integer
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *current_node = *head;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
	{
		free(new_node);
		return (NULL);
	}
	new_node->n = number;
	new_node->next = NULL;
	if (*head == NULL)
	{
		*head = new_node;
		return (new_node);
	}
	while (current_node != NULL)
	{
		if (current_node->n > number)
		{
			new_node->next = current_node;
			*head = new_node;
			return (new_node);
		}
		else if (current_node->next != NULL
			 && number < current_node->next->n)
		{
			new_node->next = current_node->next;
			current_node->next = new_node;
			return (new_node);
		}
		if (current_node->next == NULL)
		{
			current_node->next = new_node;
			return (new_node);
		}
		current_node = current_node->next;
	}
	free(new_node);
	return (NULL);
}
