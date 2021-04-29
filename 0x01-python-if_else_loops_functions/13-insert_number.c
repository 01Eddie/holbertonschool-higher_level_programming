#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - adds a new node at the end of a listint_t list
 * @head: pointer to pointer of first node of listint_t list
 * @number: integer to be included in new node
 * Return: address of the new element or NULL if it fails
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *prev;
	listint_t *current  = *head;

	if (head == NULL)
		return (NULL);
	new_node = malloc(sizeof(*new_node));

	if (new_node == NULL)
		return (NULL);
	new_node->next = NULL;
	new_node->n = number;

	if (current == NULL || current->n > number)
	{
		new_node->next = current;
		*head = new_node;
		return (new_node);
	}

	while (current->n < number && current)
	{
		prev = current;
		current = current->next;
	}
		new_node->next = current;
		prev->next = new_node;

		return (new_node);
}
