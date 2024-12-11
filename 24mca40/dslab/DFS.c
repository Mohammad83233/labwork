#include <stdio.h>
#include <stdlib.h>

#define WHITE 0 // Vertex has not been visited
#define GRAY 1 // Vertex is being visited
#define BLACK 2 // Vertex and its neighbors are fully processed

typedef struct Node {
    int vertex;
    struct Node* next;
} Node;

typedef struct Graph {
    int numVertices;
    Node** adjLists;
    int* color;
    int* discovery;
    int* finish;
    int* parent;
    int time;
} Graph;

// Function to create a new node
Node* createNode(int v) {
    Node* newNode = (Node*)malloc(sizeof(Node));
    newNode->vertex = v;
    newNode->next = NULL;
    return newNode;
}

// Function to create a graph
Graph* createGraph(int vertices) {
    Graph* graph = (Graph*)malloc(sizeof(Graph));
    graph->numVertices = vertices;
    graph->adjLists = (Node**)malloc(vertices * sizeof(Node*));
    graph->color = (int*)malloc(vertices * sizeof(int));
    graph->discovery = (int*)malloc(vertices * sizeof(int));
    graph->finish = (int*)malloc(vertices * sizeof(int));
    graph->parent = (int*)malloc(vertices * sizeof(int));
    graph->time = 0;

    for (int i = 0; i < vertices; i++) {
        graph->adjLists[i] = NULL;
        graph->color[i] = WHITE;
        graph->discovery[i] = -1;
        graph->finish[i] = -1;
        graph->parent[i] = -1;
    }
    return graph;
}

// Function to add an edge to the graph
void addEdge(Graph* graph, int src, int dest) {
    Node* newNode = createNode(dest);
    newNode->next = graph->adjLists[src];
    graph->adjLists[src] = newNode;
}

// DFS Visit function
void dfsVisit(Graph* graph, int u) {
    graph->color[u] = GRAY;
    graph->time++;
    graph->discovery[u] = graph->time;

    Node* temp = graph->adjLists[u];
    while (temp != NULL) {
        int v = temp->vertex;
        if (graph->color[v] == WHITE) {
            graph->parent[v] = u;
            dfsVisit(graph, v);
        }
        temp = temp->next;
    }

    graph->color[u] = BLACK;
    graph->time++;
    graph->finish[u] = graph->time;
}

// DFS Function
void dfs(Graph* graph) {
    for (int u = 0; u < graph->numVertices; u++) {
        if (graph->color[u] == WHITE) {
            dfsVisit(graph, u);
        }
    }

    // Print discovery and finish times
    printf("\nVertex Discovery Time Finish Time Parent\n");
    for (int i = 0; i < graph->numVertices; i++) {
        printf("%d %d %d %d\n", i, graph->discovery[i], graph->finish[i], graph->parent[i]);
    }
}

// Main function
int main() {
    int vertices, edges, src, dest;

    printf("Enter the number of vertices: ");
    scanf("%d", &vertices);

    Graph* graph = createGraph(vertices);

    printf("Enter the number of edges: ");
    scanf("%d", &edges);

    printf("Enter the edges (source destination):\n");
    for (int i = 0; i < edges; i++) {
        scanf("%d %d", &src, &dest);
        addEdge(graph, src, dest);
    }

    printf("\nDFS Execution:");
    dfs(graph);

    return 0;
}

