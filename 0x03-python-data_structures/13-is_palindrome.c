#include "lists.h"

/**
 * is_palindrome - frees a listint_t list
 * @head: pointer to list to be freed
 * Return: 0 or 1
 */

int is_palindrome(listint_t **head)
{
	listint_t *slow_ptr = *head, *fast_ptr = *head;
	listint_t *second_half, *prev_of_slow_ptr = *head;
	listint_t *midnode = NULL;
	int res = 0;

	if (*head != NULL && *head->next != NULL)
	{
		while (fast_ptr != NULL && fast_ptr->next != NULL)
		{
			fast_ptr = fast_ptr->next->next;
			prev_of_slow_ptr = slow_ptr;
			slow_ptr = slow_ptr->next;
		}
		if (fast_ptr != NULL)
		{
			midnode = slow_ptr;
			slow_ptr = slow_ptr->next;
		}
		second_half = slow_ptr;
		prev_of_slow_ptr->next = NULL;
		reverse(&second_half);
		res = compareLists(*head, second_half);
		reverse(&second_half);

		if (midnode != NULL)
		{
			prev_of_slow_ptr->next = midnode;
			midnode->next = second_half;
		}
		else
			prev_of_slow_ptr->next = second_half;
	}
	return (res);
}
