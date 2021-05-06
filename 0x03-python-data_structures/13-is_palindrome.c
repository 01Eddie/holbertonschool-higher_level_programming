#include "lists.h"

/**
 * reverse_list - function name
 * @h: head of list
 *
 * Return: reverse list
 */
listint_t *reverse_list(listint_t **h)
{
	listint_t *tmp1, *tmp2, *tmp3;

	tmp1 = *h;
	tmp2 = NULL;

	while (tmp1)
	{
		tmp3 = tmp1->next;
		tmp1->next = tmp2;
		tmp2 = tmp1;
		tmp1 = tmp3;
	}
	*h = tmp2;
	return (*h);
}
/**
 * is_palindrome - frees a listint_t list
 * @head: pointer to list to be freed
 * Return: 0 or 1
 */

int is_palindrome(listint_t **head)
{
	listint_t *tmp1, *tmp2;
	int nodes, i;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	tmp1 = *head;
	for (nodes = 0; tmp1; nodes++)
		tmp1 = tmp1->next;
	tmp1 = *head;
	if (nodes % 2 != 0)
		tmp1 = tmp1->next;

	tmp2 = reverse_list(&tmp1);
	tmp1 = *head;

	while (tmp2)
	{
		if (tmp1->n != tmp2->n)
			return (0);
		tmp1 = tmp1->next;
		tmp2 = tmp2->next;
	}
	return (1);
}
