// undirected graph
// depth first search - traversal 

#include<vector>
#include<iostream>

using namespace std;
class Solution {

private: 

    // depth first search traversal 
    void dfs(int node, vector<int> adj[], int visitedNodes[], vector<int> &list_dfs)
    {
        cout << "entering dfs function\n ";
        visitedNodes[node] = 1;
        list_dfs.push_back(node);

        for(auto it : adj[node])
        {
            if(!visitedNodes[it])
                dfs(it, adj, visitedNodes, list_dfs);
        }
    }
public:

    // calculate output
    vector<int> dfsGraph(int V, vector<int> adj[])
    {
        cout << "test \n";
        int visitedNodes[V] = {0};
        int startNode = 1;
        vector<int> list_dfs;
        cout << "before calling dfs \n";
        dfs(startNode, adj, visitedNodes, list_dfs);

        return list_dfs;
    }
};

int main()
{
    //provide input
    int V = 5;
    vector<int> adj[V];
    adj[0] = {1,2};
    adj[1] = {0,3,4};
    adj[2] = {0};
    adj[3] = {1};
    adj[4] = {1};

    // calculate output
    Solution sol;
    cout << "started main function \n";
    vector<int> traversal = sol.dfsGraph(V, adj);

    // print output
    cout << "\n DFS traversal: ";
    for(int node: traversal)
        cout << node << " ";
    cout << endl;

    return 0;
}