package com.example.praveenkn.cloudmanagementclient;

import android.content.Context;
import android.support.v7.widget.RecyclerView;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.view.animation.Animation;
import android.view.animation.AnimationUtils;
import android.widget.TextView;

import com.example.praveenkn.cloudmanagementclient.ItemFragment_Projects.OnListFragmentInteractionListener;
import com.example.praveenkn.cloudmanagementclient.Models.Project;

import java.util.List;

/**
 * {@link RecyclerView.Adapter} that can display a {@link Project} and makes a call to the
 * specified {@link OnListFragmentInteractionListener}.
 * TODO: Replace the implementation with code for your data type.
 */
public class MyItemRecyclerViewAdapter extends RecyclerView.Adapter<MyItemRecyclerViewAdapter.ViewHolder> {

    private final List<Project> mValues;
    private final OnListFragmentInteractionListener mListener;
    private Context context;
    public MyItemRecyclerViewAdapter(List<Project> items, OnListFragmentInteractionListener listener, Context context) {
        mValues = items;
        mListener = listener;
        this.context=context;
    }

    @Override
    public ViewHolder onCreateViewHolder(ViewGroup parent, int viewType) {
        View view = LayoutInflater.from(parent.getContext())
                .inflate(R.layout.fragment_projectlist, parent, false);
        return new ViewHolder(view);
    }

    @Override
    public void onBindViewHolder(final ViewHolder holder, int position) {
        holder.mItem = mValues.get(position);
        holder.mContentView.setText(mValues.get(position).projectName);
        int lastPosition=-1;
        holder.mDescriptionview.setText(mValues.get(position).description);
        Animation animation = AnimationUtils.loadAnimation(context,
                (position > lastPosition) ? R.anim.animation_scroll_bottom_top
                        : R.anim.animation_scroll_top_bottom);
        holder.itemView.startAnimation(animation);
        lastPosition = position;
        holder.mView.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (null != mListener) {
                    // Notify the active callbacks interface (the activity, if the
                    // fragment is attached to one) that an item has been selected.
                    mListener.onListFragmentInteraction(holder.mItem);
                }
            }
        });
    }

    @Override
    public int getItemCount() {
        return mValues.size();
    }

    public class ViewHolder extends RecyclerView.ViewHolder {
        public final View mView;
        public final TextView mContentView;
        public final TextView mDescriptionview;
        public Project mItem;

        public ViewHolder(View view) {
            super(view);
            mView = view;
            mDescriptionview=(TextView)view.findViewById(R.id.descriptionTxtView);
            mContentView = (TextView) view.findViewById(R.id.projectNameTextView);
        }

        @Override
        public String toString() {
            return super.toString() + " '" + mContentView.getText() + "'";
        }
    }

}
