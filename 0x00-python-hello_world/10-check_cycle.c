#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - Function that checks if a singly linked list has a cycle in it
 * @list: pointer type listint_t
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *first_node = list, *current_node = list;

	while (current_node != NULL)
	{
		if (current_node->next == first_node)
			return (1);

		current_node = current_node->next;
	}

	return (0);
}
