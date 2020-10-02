#include <bits/stdc++.h>
using namespace std;

vector <int> adj[101];
bool visited[101];
void addEdge(int x , int y)
{
	//Undirected Graph
	adj[x].push_back(y);                   //Edge from vertex x to vertex y
	adj[y].push_back(x);				  //Edge from vertex y to vertex x
}
void dfs(int s) {
	visited[s] = true;
	for (int i = 0; i < adj[s].size(); ++i)    {
		if (visited[adj[s][i]] == false)
			dfs(adj[s][i]);
	}
}

int main() {
#ifndef ONLINE_JUDGE
	freopen("/home/kushagra/Desktop/Kushagra/input.txt", "r", stdin);
	freopen("/home/kushagra/Desktop/Kushagra/output.txt", "w", stdout);
#endif
	int nodes, edges, x, y, connectedComponents = 0;
	cin >> nodes;                       //Number of nodes
	cin >> edges;                       //Number of edges
	memset(visited, false, sizeof(visited));
	for (int i = 0; i < edges; ++i) {
		cin >> x >> y;
		//Undirected Graph
		addEdge(x, y);
	}
	//if dfs in i is applied then all the vertices of i will be maarked true and then if any other node is left then
	//we will make that node as i and apply dfs to that node
	for (int i = 1; i <= nodes; ++i)
	{
		if (visited[i] == false)
		{
			dfs(i);
			connectedComponents++;
		}
	}
	cout << "connectedComponents in a graph is : " << connectedComponents;
	return 0;
}

/*
6
4
1 2
2 3
1 3
4 5
o/p-
connectedComponents in a graph is : 3
*/