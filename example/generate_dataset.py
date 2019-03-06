from deeprank.generate import *


# name of the hdf5 to generate
h5file = ['1ak4.hdf5','native.hdf5']

# for each hdf5 file where to find the pdbs
pdb_source     = ['../test/1AK4/decoys/','../test/1AK4/native/']

# where to find the native conformations
# pdb_native is only used to calculate i-RMSD, dockQ and so on.
#The native pdb files will not be saved in the hdf5 file
pdb_native     = ['../test/1AK4/native/']


# where to find the pssm
pssm_source = '../test/1AK4/pssm_new/'

# loop over the dataset to create
for h5,src in zip(h5file,pdb_source):

    # initialize the database
    database = DataGenerator(pdb_source=src,
                             pdb_native=pdb_native,
                             pssm_source=pssm_source,
                             data_augmentation = 1,
                             compute_targets  = ['deeprank.targets.dockQ','deeprank.targets.binary_class'],
                             compute_features = ['deeprank.features.AtomicFeature',
                                                 'deeprank.features.FullPSSM',
                                                 'deeprank.features.PSSM_IC',
                                                 'deeprank.features.BSA',
                                                 'deeprank.features.ResidueDensity'],
                             hdf5=h5)


    # create the database
    # compute features/targets for all complexes
    print('{:25s}'.format('Create new database') + database.hdf5)
    database.create_database(prog_bar=True)


    # define the 3D grid
    grid_info = {
        'number_of_points' : [30,30,30],
        'resolution' : [1.,1.,1.],
        'atomic_densities' : {'CA':3.5,'N':3.5,'O':3.5,'C':3.5},
    }

    # map the features to the 3D grid
    print('{:25s}'.format('Map features in database') + database.hdf5)
    database.map_features(grid_info,try_sparse=True, time=False, prog_bar=True)


    # get the normalization of the features
    print('{:25s}'.format('Normalization') + database.hdf5)
    norm = NormalizeData(h5)
    norm.get()
