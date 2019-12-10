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
	listint_t *node_1 = list, *node_2 = list;

	while (node_1 && node_2 && node_2->next)
	{
		node_1 = node_1->next;
		node_2 = node_2->next->next;

		if (node_1 == node_2)
			return (1);
	}

	return (0);
}
