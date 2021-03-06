#region GPLv3 notice
# Copyright 2014 Damian Quiroga
#
# This file is part of dissect.
#
# dissect is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# dissect is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with dissect.  If not, see <http://www.gnu.org/licenses/>.
#endregion

from nose.tools import *

from dissect.model.util.tree import TreeRootNode, TreeNode


class TestTreeNode():
    def test_the_root_node_has_no_parent(self):
        assert_equal(TreeRootNode().parent, None)

    def test_the_root_node_is_created_with_no_children(self):
        assert_equal(TreeRootNode().children, [])

    def test_the_root_node_has_branch_depth_zero(self):
        assert_equal(TreeRootNode().branch_depth, 0)

    def test_a_regular_node_must_have_a_parent(self):
        assert_raises(TypeError, TreeNode)

    def test_a_child_of_the_root_node_can_access_its_parent(self):
        root_node = TreeRootNode()
        node = TreeNode(root_node)
        assert_equal(node.parent, root_node)

    def test_a_regular_node_can_access_its_parent(self):
        root_node = TreeRootNode()
        node1 = TreeNode(root_node)
        node2 = TreeNode(node1)
        assert_equal(node2.parent, node1)

    def test_the_root_node_can_have_one_child(self):
        root_node = TreeRootNode()
        node = TreeNode(root_node)
        assert_equal(root_node.children, [node])

    def test_the_root_node_can_have_two_children(self):
        root_node = TreeRootNode()
        node1 = TreeNode(root_node)
        node2 = TreeNode(root_node)
        assert_equal(root_node.children, [node1, node2])

    def test_a_regular_node_can_have_one_child(self):
        root_node = TreeRootNode()
        node1 = TreeNode(root_node)
        node2 = TreeNode(node1)
        assert_equal(node1.children, [node2])

    def test_a_regular_node_can_have_two_children(self):
        root_node = TreeRootNode()
        node1 = TreeNode(root_node)
        node2 = TreeNode(node1)
        node3 = TreeNode(node1)
        assert_equal(node1.children, [node2, node3])

    def test_a_child_of_the_root_node_has_branch_depth_one(self):
        root_node = TreeRootNode()
        node = TreeNode(root_node)
        assert_equal(node.branch_depth, 1)

    def test_a_grandchild_of_the_root_node_has_branch_depth_two(self):
        root_node = TreeRootNode()
        child = TreeNode(root_node)
        grandchild = TreeNode(child)
        assert_equal(grandchild.branch_depth, 2)
