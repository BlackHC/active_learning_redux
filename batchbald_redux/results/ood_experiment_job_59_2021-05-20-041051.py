store = {}
store['timestamp']=1621480251
store['cmdline']=['/home/kell4989/git/active_learning_redux/batchbald_redux/ood_experiment.py', '--id=59']
store['commit']='8a2cf4fb40ce306533b4e439b08268c53f009a3b'
store['github_url']='8a2cf4fb40ce306533b4e439b08268c53f009a3b'
store['experiment']='/home/kell4989/git/active_learning_redux/batchbald_redux/ood_experiment.py'
store['job_id']=59
store['worker_id']=59
store['num_workers']=80
store['config']={'seed': 1296, 'uniform_ood': False, 'id_dataset_type': 'batchbald_redux.fast_mnist.FastFashionMNIST', 'ood_dataset_type': 'batchbald_redux.fast_mnist.FastMNIST', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 16, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastFashionMNIST (train; 58976 samples)) + ('FastMNIST Train (60000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'FastFashionMNIST Test (10000 samples)'"}
store['initial_training_set_indices']=[55573, 380, 12640, 44119, 30392, 58226, 43812, 52440, 3091, 29974, 49512, 46037, 53434, 22015, 37915, 52296, 8533, 58125, 22304, 35472]
store['evaluation_set_indices']=[42890, 14640, 45567, 52801, 53689, 801, 55187, 26479, 50997, 3792]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 2.4372429847717285})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 2.9417476654052734})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 3.0509395599365234})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 3.715665817260742})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 3.544271469116211})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 3.81615948677063})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 3.9685420989990234})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 3.913039207458496})
store['active_learning_steps'][0]['training']['best_epoch']=5
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6171, 'crossentropy': 3.770203515625}
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 46777], ['id', 35930], ['id', 42309], ['id', 27863], ['id', 39451]], 'labels': [-1, -1, -1, 2, -1], 'scores': [1.6567381084522617, 2.86104475010118, 3.7273068345075195, 4.224476817741632, 4.451315889205124]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 2.297114372253418})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 2.957777976989746})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 3.5735626220703125})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 3.6028060913085938})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.5957, 'crossentropy': 2.4495720703125}
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 51902], ['id', 47260], ['id', 55778], ['id', 37777], ['id', 45998]], 'labels': [-1, -1, 8, -1, -1], 'scores': [1.3264717333020366, 2.369122695860825, 3.1557210818695642, 3.7186228238299606, 4.074752502952785]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 2.2599313259124756})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 2.858522653579712})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.5869140625, 'crossentropy': 3.16894268989563})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 3.758974552154541})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.6085, 'crossentropy': 2.2833865234375}
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 57543], ['id', 45148], ['id', 32731], ['id', 19429], ['id', 54813]], 'labels': [-1, -1, -1, -1, 8], 'scores': [1.3658917936039026, 2.4584608351877617, 3.1936168868496253, 3.7273093341589654, 4.066580829492882]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.5849609375, 'crossentropy': 2.57281494140625})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 3.298015594482422})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.587890625, 'crossentropy': 3.523379325866699})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 3.434321403503418})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.5888671875, 'crossentropy': 3.6612391471862793})
store['active_learning_steps'][3]['training']['best_epoch']=2
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.5772, 'crossentropy': 3.507873828125}
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 27181], ['id', 49373], ['id', 32856], ['id', 22774], ['id', 22677]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5517661187720493, 2.7340545244549, 3.521381615575236, 4.019174547033268, 4.296550316365776]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.583984375, 'crossentropy': 2.258087635040283})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.58203125, 'crossentropy': 2.6213252544403076})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 3.4039688110351562})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 3.1737477779388428})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 4.236654281616211})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 3.6796274185180664})
store['active_learning_steps'][4]['training']['best_epoch']=3
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.6013, 'crossentropy': 3.484108984375}
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 13326], ['id', 28248], ['id', 23765], ['id', 37113], ['id', 34620]], 'labels': [-1, -1, -1, -1, 0], 'scores': [1.5309375543143848, 2.762349511515626, 3.664606960101893, 4.131276015977511, 4.372871633233452]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 2.262758731842041})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 2.8723440170288086})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.5810546875, 'crossentropy': 3.4417099952697754})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 3.716451644897461})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 3.7677230834960938})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 3.9233720302581787})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 3.8550052642822266})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 4.227860450744629})
store['active_learning_steps'][5]['training']['best_epoch']=5
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.5883, 'crossentropy': 3.913316796875}
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 11642], ['id', 51596], ['id', 47636], ['id', 22937], ['id', 13588]], 'labels': [-1, -1, -1, 9, -1], 'scores': [1.5022235052930837, 2.7970677887636892, 3.6906114248701414, 4.157612288407618, 4.395690355461994]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 2.1861391067504883})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 2.8012280464172363})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 3.07098388671875})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 3.148103952407837})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 3.852206230163574})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 4.185762405395508})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 3.536609172821045})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 3.8608131408691406})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.5927734375, 'crossentropy': 4.035277366638184})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.58203125, 'crossentropy': 3.7311534881591797})
store['active_learning_steps'][6]['training']['best_epoch']=7
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.5874, 'crossentropy': 4.06407890625}
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 1574], ['id', 54196], ['id', 27130], ['id', 35930], ['id', 22652]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.6112372307499174, 2.7838218831898622, 3.6274513941936997, 4.116717306733836, 4.379968575701547]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 2.198115825653076})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 2.7600624561309814})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 3.047240734100342})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 3.2074034214019775})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 3.2951860427856445})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 3.8195924758911133})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 3.6550283432006836})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 3.921625852584839})
store['active_learning_steps'][7]['training']['best_epoch']=5
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.598, 'crossentropy': 3.564019921875}
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 19697], ['id', 38630], ['id', 40899], ['id', 17041], ['id', 39793]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.623766043109621, 2.8523061314193705, 3.6886750879847243, 4.160325998894864, 4.389311246139458]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 1.9944965839385986})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 2.5604248046875})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 3.1108217239379883})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 3.5844197273254395})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 3.470860719680786})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 3.859912872314453})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 3.7033114433288574})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.1564927101135254})
store['active_learning_steps'][8]['training']['best_epoch']=5
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.5983, 'crossentropy': 3.675863671875}
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 28501], ['id', 1225], ['id', 32144], ['id', 57632], ['id', 41438]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.6268612399446591, 2.9074063780964563, 3.7461452088792555, 4.220755899888678, 4.439244183883226]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 2.002199172973633})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.580078125, 'crossentropy': 3.352242946624756})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 3.179654598236084})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 3.105691909790039})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.5908203125, 'crossentropy': 3.434927225112915})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 3.219271183013916})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 3.664609432220459})
store['active_learning_steps'][9]['training']['best_epoch']=4
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.609, 'crossentropy': 3.444175390625}
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 36379], ['id', 1789], ['id', 45324], ['id', 38600], ['id', 55278]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.6670842421626197, 2.8282808739473015, 3.6614007855380137, 4.144127011031539, 4.4021754917323666]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 2.1948537826538086})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.58203125, 'crossentropy': 3.2027153968811035})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.5859375, 'crossentropy': 3.7277605533599854})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.583984375, 'crossentropy': 3.7351794242858887})
store['active_learning_steps'][10]['training']['best_epoch']=1
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.6075, 'crossentropy': 2.3437724609375}
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 20379], ['id', 31778], ['id', 3362], ['id', 4743], ['id', 16722]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.343682756225538, 2.3881431874781684, 3.1692653474316845, 3.710364553742461, 4.058736626136986]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 2.2792930603027344})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.5849609375, 'crossentropy': 2.872208833694458})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 3.4569315910339355})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 3.271071434020996})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 3.370062828063965})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 3.2166738510131836})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 3.8112525939941406})
store['active_learning_steps'][11]['training']['best_epoch']=4
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.5942, 'crossentropy': 3.812412109375}
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 28173], ['id', 34829], ['id', 9458], ['id', 41802], ['id', 31744]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5522137097106072, 2.7779112373295543, 3.6230355493570965, 4.122103562992958, 4.3830391298140965]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 2.219686985015869})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 2.9082443714141846})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 2.9680240154266357})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 3.637996196746826})
store['active_learning_steps'][12]['training']['best_epoch']=1
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.6101, 'crossentropy': 2.093378515625}
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 8768], ['id', 30281], ['id', 50517], ['id', 57132], ['id', 50315]], 'labels': [-1, -1, -1, 0, -1], 'scores': [1.2976985426837095, 2.3398381915479423, 3.1385647405107857, 3.667433365256988, 4.028972558514804]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 2.1741936206817627})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 2.6494274139404297})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 3.0268216133117676})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 3.4778409004211426})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 3.346907615661621})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 3.5034525394439697})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 3.85351300239563})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 3.8411364555358887})
store['active_learning_steps'][13]['training']['best_epoch']=5
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.5991, 'crossentropy': 3.56711796875}
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 59392], ['id', 57726], ['id', 9056], ['id', 45558], ['id', 15382]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5578376224996378, 2.920482610445213, 3.766218046281626, 4.215153400051146, 4.415480728940053]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.5869140625, 'crossentropy': 2.012751340866089})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.5859375, 'crossentropy': 2.7091212272644043})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 3.3139545917510986})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 3.55491304397583})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.576171875, 'crossentropy': 3.522400140762329})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 3.4087207317352295})
store['active_learning_steps'][14]['training']['best_epoch']=3
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.5789, 'crossentropy': 3.430483203125}
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 2034], ['id', 19931], ['id', 1254], ['id', 43823], ['id', 32131]], 'labels': [-1, -1, 0, -1, -1], 'scores': [1.5831703376036261, 2.7974407017935086, 3.6367723545213257, 4.157600123408835, 4.403890722437195]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 2.194093704223633})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 2.538395881652832})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 3.04270076751709})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 3.629578113555908})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 3.135960817337036})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 3.1271109580993652})
store['active_learning_steps'][15]['training']['best_epoch']=3
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.5986, 'crossentropy': 3.1549474609375}
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 56484], ['id', 18799], ['id', 39855], ['id', 58419], ['id', 48621]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.430687726378994, 2.577512298118804, 3.432486312677229, 3.9844726415658176, 4.278886241634828]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 1.9633986949920654})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 2.4314990043640137})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 2.78513240814209})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 2.980184555053711})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.5927734375, 'crossentropy': 3.106004238128662})
store['active_learning_steps'][16]['training']['best_epoch']=2
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.6046, 'crossentropy': 2.6639177734375}
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 46846], ['id', 12345], ['id', 13769], ['id', 58390], ['id', 4577]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5088027594455533, 2.6180433751247776, 3.3968145012641475, 3.9240585381933, 4.239540733001331]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 2.0797128677368164})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 2.2221460342407227})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.5703125, 'crossentropy': 3.3533248901367188})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 3.122073173522949})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 3.1314103603363037})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 3.2460155487060547})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.58203125, 'crossentropy': 3.9171056747436523})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 3.242952823638916})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 3.812645673751831})
store['active_learning_steps'][17]['training']['best_epoch']=6
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.5848, 'crossentropy': 3.523603515625}
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 56094], ['id', 4827], ['id', 40162], ['id', 42681], ['id', 43105]], 'labels': [-1, -1, -1, -1, 5], 'scores': [1.5842944333205304, 2.835393949591097, 3.688015058887503, 4.164014124979804, 4.409073822704052]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.587890625, 'crossentropy': 2.2784063816070557})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 2.7818775177001953})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 2.8394665718078613})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 2.964428186416626})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 3.096188545227051})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 3.1744496822357178})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 3.1876187324523926})
store['active_learning_steps'][18]['training']['best_epoch']=4
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.5994, 'crossentropy': 3.384339453125}
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 31942], ['id', 18483], ['id', 32397], ['id', 34780], ['id', 55278]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5214334655500061, 2.712633160096978, 3.5567302713857174, 4.051449404224767, 4.322716190092349]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.5771484375, 'crossentropy': 2.0073750019073486})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 2.7122862339019775})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 3.066495418548584})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 3.009080410003662})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 3.173638343811035})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 3.1331045627593994})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.464859962463379})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 3.139010190963745})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 3.3742175102233887})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 3.217160701751709})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 3.6181702613830566})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 3.6836514472961426})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 3.6492581367492676})
store['active_learning_steps'][19]['training']['best_epoch']=10
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.6048, 'crossentropy': 3.61853046875}
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 45243], ['id', 27509], ['id', 36091], ['id', 56691], ['id', 3573]], 'labels': [-1, -1, 2, -1, -1], 'scores': [1.559119462262246, 2.810492832136106, 3.718585884839179, 4.265784442314221, 4.467201454522037]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 1.8428881168365479})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 2.7710413932800293})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 3.1156063079833984})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 3.2416629791259766})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 3.3970751762390137})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 3.946286678314209})
store['active_learning_steps'][20]['training']['best_epoch']=3
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.605, 'crossentropy': 3.28395703125}
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 45198], ['id', 17660], ['id', 28489], ['id', 47627], ['id', 32776]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5454273597726624, 2.7242978938038744, 3.5720845441937854, 4.054553012093191, 4.33463681487928]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 2.1030516624450684})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 2.798666477203369})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 2.9301629066467285})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 3.090425491333008})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 4.160971164703369})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 3.423818826675415})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 3.6978681087493896})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.5859375, 'crossentropy': 4.578817844390869})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 3.778616428375244})
store['active_learning_steps'][21]['training']['best_epoch']=6
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.5907, 'crossentropy': 3.80510390625}
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 46877], ['id', 12287], ['id', 42433], ['id', 14578], ['id', 36252]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5318916129872426, 2.694631980173213, 3.5118831032979347, 4.05151042031946, 4.361208321747721]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.9311726093292236})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 2.590595006942749})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 3.0654525756835938})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 3.4832754135131836})
store['active_learning_steps'][22]['training']['best_epoch']=1
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.6068, 'crossentropy': 2.0511625}
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 8964], ['id', 9459], ['id', 32504], ['id', 20415], ['id', 24903]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4471699311317603, 2.5320920464274135, 3.271721132989283, 3.7893450837845277, 4.1167531039238465]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 2.282663106918335})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 2.601163625717163})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.933065414428711})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 3.234328269958496})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 3.212986707687378})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 3.336660385131836})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 3.7566943168640137})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 3.1627273559570312})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.680264711380005})
store['active_learning_steps'][23]['training']['best_epoch']=6
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.622, 'crossentropy': 3.6397640625}
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 4781], ['id', 7528], ['id', 40521], ['id', 56379], ['id', 48176]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.561896075150614, 2.953023805459204, 3.8355376412897186, 4.255998114739065, 4.45838762151965]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.5703125, 'crossentropy': 2.39996600151062})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 2.733203172683716})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 3.0871293544769287})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 3.7937169075012207})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 3.8493337631225586})
store['active_learning_steps'][24]['training']['best_epoch']=2
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.5899, 'crossentropy': 2.9710873046875}
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 31130], ['id', 13247], ['id', 27738], ['id', 55278], ['id', 16190]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.454765826422335, 2.611184434758525, 3.4732385532466408, 3.9857556161970553, 4.295172990694739]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 2.2301554679870605})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 2.585158348083496})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 2.824402332305908})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 2.8853931427001953})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 3.332987070083618})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 3.542210817337036})
store['active_learning_steps'][25]['training']['best_epoch']=3
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.6082, 'crossentropy': 2.9815095703125}
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 24810], ['id', 32507], ['id', 5641], ['id', 6598], ['id', 45056]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4258784767068222, 2.6326266449672033, 3.514892030576176, 4.010509548584476, 4.281526030027277]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.578125, 'crossentropy': 1.8912920951843262})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 2.578432083129883})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 2.920578956604004})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 3.019171714782715})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 3.4062623977661133})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 3.3532533645629883})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 3.6118969917297363})
store['active_learning_steps'][26]['training']['best_epoch']=4
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.6147, 'crossentropy': 3.162735546875}
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 27195], ['id', 4881], ['id', 46292], ['id', 6598], ['id', 1213]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5868981354255007, 2.7770172820751498, 3.6280903894677, 4.110137355721015, 4.378508004594969]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 2.0951359272003174})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 2.8815503120422363})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.5791015625, 'crossentropy': 2.915247917175293})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 3.105782985687256})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 3.078984260559082})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 3.570621967315674})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 3.7284693717956543})
store['active_learning_steps'][27]['training']['best_epoch']=4
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.5909, 'crossentropy': 3.2081927734375}
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 56094], ['id', 26778], ['id', 29712], ['id', 47987], ['id', 34798]], 'labels': [-1, -1, -1, 5, -1], 'scores': [1.6306390150989154, 2.816488418579002, 3.6682984426534455, 4.146519459016234, 4.388682651258998]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 2.1152777671813965})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 2.518925189971924})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 2.901174545288086})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 3.1981778144836426})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.215329170227051})
store['active_learning_steps'][28]['training']['best_epoch']=2
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.6249, 'crossentropy': 2.7230173828125}
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 33204], ['id', 12060], ['id', 37594], ['id', 53073], ['id', 13158]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4510800847032939, 2.7099301645084912, 3.5210683307143196, 4.0046551030020865, 4.31019547849397]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 1.9864296913146973})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 2.435333251953125})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 2.8702406883239746})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 3.020195245742798})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 3.338261604309082})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 3.353135585784912})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 3.334393262863159})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 3.8281822204589844})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 4.128518104553223})
store['active_learning_steps'][29]['training']['best_epoch']=6
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.601, 'crossentropy': 3.587886328125}
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 30287], ['id', 9963], ['id', 49212], ['id', 8676], ['id', 8031]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5843899091801785, 2.8197173433869174, 3.6383789737267698, 4.143755594590768, 4.392855390952104]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 2.2443654537200928})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 2.593550443649292})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 3.099419116973877})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 3.160433292388916})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 3.506329298019409})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 3.3664283752441406})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 3.732496738433838})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 3.875013828277588})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.5927734375, 'crossentropy': 3.624244213104248})
store['active_learning_steps'][30]['training']['best_epoch']=6
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.6034, 'crossentropy': 3.586898828125}
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 21951], ['id', 7003], ['id', 5017], ['id', 44377], ['id', 44661]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.658517303816081, 2.8965692858009184, 3.718874549831657, 4.177420071323129, 4.417858668444775]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 1.7871476411819458})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 2.3667664527893066})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 2.817643642425537})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 3.075418472290039})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 3.209622859954834})
store['active_learning_steps'][31]['training']['best_epoch']=2
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.6105, 'crossentropy': 2.5140873046875}
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 14966], ['id', 50618], ['id', 31055], ['id', 32126], ['id', 36259]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4544298334595465, 2.5546265979361604, 3.421878267948199, 3.9616930393750422, 4.241822628806483]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 1.9811882972717285})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 2.6573221683502197})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 2.8254318237304688})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 2.692448377609253})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 2.9455018043518066})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 2.9156494140625})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.4674816131591797})
store['active_learning_steps'][32]['training']['best_epoch']=4
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.6063, 'crossentropy': 3.040580078125}
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 25180], ['id', 50155], ['id', 43465], ['id', 30421], ['id', 55540]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.6903316326476334, 2.8448784741395325, 3.6857521826902673, 4.144500979263715, 4.384608749038684]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 2.0309031009674072})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 2.992504596710205})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 2.9846248626708984})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 3.2603540420532227})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 3.450075149536133})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 3.4572787284851074})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 4.086197853088379})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 4.027203559875488})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 3.718418598175049})
store['active_learning_steps'][33]['training']['best_epoch']=6
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.5996, 'crossentropy': 3.833055078125}
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 59407], ['id', 29489], ['id', 22622], ['id', 25629], ['id', 31051]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.6596139501884872, 2.8226397561926917, 3.6556070825561466, 4.153495296647569, 4.415723544295721]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 2.1635565757751465})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 2.5620861053466797})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 3.386171817779541})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 3.3080554008483887})
store['active_learning_steps'][34]['training']['best_epoch']=1
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.601, 'crossentropy': 2.2161130859375}
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 9709], ['id', 9251], ['id', 59747], ['id', 52830], ['id', 22960]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.2094116968974642, 2.2142514549314254, 2.954411549484675, 3.503253276189743, 3.8847608213342504]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 2.08754301071167})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 2.7524356842041016})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 3.189197540283203})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 3.382711410522461})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 3.208357572555542})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 3.664008140563965})
store['active_learning_steps'][35]['training']['best_epoch']=3
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.6034, 'crossentropy': 3.1470671875}
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 42377], ['id', 5465], ['id', 25475], ['id', 15932], ['id', 16948]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.446948920722921, 2.737076697465935, 3.564301962270723, 4.075726769413581, 4.356341987830075]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 2.032594680786133})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 2.556215286254883})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 2.808974266052246})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 3.19840669631958})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 3.389072895050049})
store['active_learning_steps'][36]['training']['best_epoch']=2
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.5893, 'crossentropy': 2.74722109375}
store['active_learning_steps'][36]['acquisition']={'indices': [['id', 3573], ['id', 54435], ['id', 35930], ['id', 4737], ['id', 39130]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.3923499399504158, 2.5330946074760954, 3.38458676172036, 3.934839319062025, 4.229867986716838]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 2.1476666927337646})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 2.796234130859375})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 3.170469284057617})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 3.1230292320251465})
store['active_learning_steps'][37]['training']['best_epoch']=1
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.6087, 'crossentropy': 2.2404013671875}
store['active_learning_steps'][37]['acquisition']={'indices': [['id', 9388], ['id', 22622], ['id', 32232], ['id', 6919], ['id', 56348]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.3564819638327972, 2.367050928793925, 3.1355214591030958, 3.6652390084040736, 4.015623612177537]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 1.9584165811538696})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 2.2934932708740234})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.49521541595459})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 2.6884756088256836})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 2.877725124359131})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 2.9702682495117188})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 3.158421516418457})
store['active_learning_steps'][38]['training']['best_epoch']=4
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.6318, 'crossentropy': 2.818841015625}
store['active_learning_steps'][38]['acquisition']={'indices': [['id', 18228], ['id', 7440], ['id', 18665], ['id', 2309], ['id', 17303]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.511441164188229, 2.79322208533354, 3.6289372838802523, 4.111869193141688, 4.35392322486901]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 1.9571658372879028})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 2.541898250579834})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 2.707731008529663})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 3.3119075298309326})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 2.828878402709961})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 3.643691062927246})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 3.705721378326416})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 3.7211244106292725})
store['active_learning_steps'][39]['training']['best_epoch']=5
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.6125, 'crossentropy': 3.2072734375}
store['active_learning_steps'][39]['acquisition']={'indices': [['id', 9709], ['id', 48527], ['id', 11193], ['id', 12940], ['id', 51427]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.638794559338514, 2.89204753652692, 3.703162877124865, 4.174043534546636, 4.410108419730268]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 1.9446724653244019})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.5830078125, 'crossentropy': 2.6595935821533203})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 3.0998220443725586})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 3.3829522132873535})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 3.7672877311706543})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 3.5166711807250977})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 3.36728572845459})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 3.5897700786590576})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 3.6828393936157227})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 4.07675838470459})
store['active_learning_steps'][40]['training']['best_epoch']=7
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.6105, 'crossentropy': 3.4361046875}
store['active_learning_steps'][40]['acquisition']={'indices': [['id', 51910], ['id', 14787], ['id', 28611], ['id', 36475], ['id', 27720]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5600355495315754, 2.6790277412792696, 3.5126735226118573, 4.042221798051453, 4.336417841488342]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 2.122420310974121})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 2.6747443675994873})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 2.9374959468841553})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 2.965318202972412})
store['active_learning_steps'][41]['training']['best_epoch']=1
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.5903, 'crossentropy': 2.1468546875}
store['active_learning_steps'][41]['acquisition']={'indices': [['id', 28109], ['id', 22647], ['id', 23124], ['id', 7490], ['id', 7596]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.3108936231305464, 2.2784230627398214, 3.066576956753634, 3.595787838158632, 3.953092654730745]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 1.9616992473602295})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 2.516110420227051})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 2.9712042808532715})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.988722801208496})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 3.373033046722412})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 3.532437801361084})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 3.635880947113037})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 3.5803897380828857})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 3.7164745330810547})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.107755661010742})
store['active_learning_steps'][42]['training']['best_epoch']=7
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.6168, 'crossentropy': 3.948255078125}
store['active_learning_steps'][42]['acquisition']={'indices': [['id', 906], ['id', 50396], ['id', 14306], ['id', 22929], ['id', 29379]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5732486542303432, 2.836722612273949, 3.7157599430887114, 4.193603832601848, 4.424798435412696]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.0217418670654297})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 2.333174705505371})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 2.7615609169006348})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 3.1815407276153564})
store['active_learning_steps'][43]['training']['best_epoch']=1
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.6123, 'crossentropy': 2.041354296875}
store['active_learning_steps'][43]['acquisition']={'indices': [['id', 25830], ['id', 42965], ['id', 56080], ['id', 48437], ['id', 8238]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.3140275451701986, 2.3322450546100875, 3.1360716622624203, 3.67982172154023, 4.0400641807876605]}
store['active_learning_steps'].append({})
store['active_learning_steps'][44]['training']={}
store['active_learning_steps'][44]['training']['epochs']=[]
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.8213865756988525})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.214508056640625})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 2.635857105255127})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 3.1305582523345947})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 3.397627830505371})
store['active_learning_steps'][44]['training']['best_epoch']=2
store['active_learning_steps'][44]['evaluation_metrics']={'accuracy': 0.6215, 'crossentropy': 2.4035658203125}
store['active_learning_steps'][44]['acquisition']={'indices': [['id', 10539], ['id', 7025], ['id', 13259], ['id', 19217], ['id', 1189]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4439453443953116, 2.5468387804804506, 3.3621591847286663, 3.9059773151804524, 4.226648410372443]}
store['active_learning_steps'].append({})
store['active_learning_steps'][45]['training']={}
store['active_learning_steps'][45]['training']['epochs']=[]
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.5654296875, 'crossentropy': 2.079803943634033})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 2.599630355834961})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 3.0094525814056396})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 3.295083999633789})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 3.316349983215332})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 3.1631546020507812})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 3.2589712142944336})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.49369478225708})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 3.555211067199707})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 3.6306161880493164})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 3.6752190589904785})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 3.6752138137817383})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 3.79445743560791})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 3.0556719303131104})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 3.5463156700134277})
store['active_learning_steps'][45]['training']['best_epoch']=12
store['active_learning_steps'][45]['evaluation_metrics']={'accuracy': 0.6209, 'crossentropy': 3.9100171875}
store['active_learning_steps'][45]['acquisition']={'indices': [['id', 27424], ['id', 41051], ['id', 14], ['id', 18228], ['id', 39279]], 'labels': [-1, -1, -1, -1, 2], 'scores': [1.5411156402853026, 2.6945700882313908, 3.584684737268768, 4.0868952148449855, 4.362918900282679]}
store['active_learning_steps'].append({})
store['active_learning_steps'][46]['training']={}
store['active_learning_steps'][46]['training']['epochs']=[]
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 1.7477353811264038})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.335035800933838})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 2.6065587997436523})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.499307632446289})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 2.894364833831787})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.326390266418457})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 3.193878173828125})
store['active_learning_steps'][46]['training']['best_epoch']=4
store['active_learning_steps'][46]['evaluation_metrics']={'accuracy': 0.6193, 'crossentropy': 2.677002734375}
store['active_learning_steps'][46]['acquisition']={'indices': [['id', 25903], ['id', 44712], ['id', 9035], ['id', 12805], ['id', 3980]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4576162549425162, 2.575660437633638, 3.462462585785606, 4.0292458385272, 4.299308487163022]}
store['active_learning_steps'].append({})
store['active_learning_steps'][47]['training']={}
store['active_learning_steps'][47]['training']['epochs']=[]
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 2.0841012001037598})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 2.5159754753112793})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 2.7102551460266113})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 3.0793020725250244})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 3.19509220123291})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 3.177896499633789})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 3.395496129989624})
store['active_learning_steps'][47]['training']['best_epoch']=4
store['active_learning_steps'][47]['evaluation_metrics']={'accuracy': 0.6016, 'crossentropy': 3.2499001953125}
store['active_learning_steps'][47]['acquisition']={'indices': [['id', 30283], ['id', 29621], ['id', 10269], ['id', 36562], ['id', 18976]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.53862117791664, 2.721828237686217, 3.5187549529698483, 4.030225754695284, 4.302883787051169]}
store['active_learning_steps'].append({})
store['active_learning_steps'][48]['training']={}
store['active_learning_steps'][48]['training']['epochs']=[]
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 2.122734785079956})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 2.3251471519470215})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 2.631025791168213})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.5869140625, 'crossentropy': 3.619656562805176})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 2.836576461791992})
store['active_learning_steps'][48]['training']['best_epoch']=2
store['active_learning_steps'][48]['evaluation_metrics']={'accuracy': 0.6081, 'crossentropy': 2.56770625}
store['active_learning_steps'][48]['acquisition']={'indices': [['id', 30287], ['id', 51714], ['id', 49429], ['id', 25520], ['id', 59257]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4596745265993958, 2.5688654101867754, 3.382618079623512, 3.9237462658929942, 4.243692994317467]}
store['active_learning_steps'].append({})
store['active_learning_steps'][49]['training']={}
store['active_learning_steps'][49]['training']['epochs']=[]
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.57421875, 'crossentropy': 2.03853440284729})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 2.2663521766662598})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 2.6259899139404297})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 3.4855966567993164})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 3.14229154586792})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 3.324366569519043})
store['active_learning_steps'][49]['training']['best_epoch']=3
store['active_learning_steps'][49]['evaluation_metrics']={'accuracy': 0.6027, 'crossentropy': 2.82789921875}
store['active_learning_steps'][49]['acquisition']={'indices': [['id', 15679], ['id', 41846], ['id', 13259], ['id', 22252], ['id', 23421]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.499366704499813, 2.741239889359724, 3.580052327822558, 4.080075279046362, 4.364652833552836]}
store['active_learning_steps'].append({})
store['active_learning_steps'][50]['training']={}
store['active_learning_steps'][50]['training']['epochs']=[]
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.58984375, 'crossentropy': 2.0771584510803223})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.5810546875, 'crossentropy': 3.0382137298583984})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.5908203125, 'crossentropy': 2.999433994293213})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.58984375, 'crossentropy': 3.5998411178588867})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 3.570727825164795})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 3.792501449584961})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 3.842209577560425})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 4.391263484954834})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 3.8326334953308105})
store['active_learning_steps'][50]['training']['best_epoch']=6
store['active_learning_steps'][50]['evaluation_metrics']={'accuracy': 0.5948, 'crossentropy': 3.95811796875}
store['active_learning_steps'][50]['acquisition']={'indices': [['id', 19789], ['id', 55774], ['id', 7406], ['id', 36147], ['id', 46579]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.644860232225156, 2.9192353859924234, 3.8636376042080354, 4.317757587005413, 4.49722127353823]}
store['active_learning_steps'].append({})
store['active_learning_steps'][51]['training']={}
store['active_learning_steps'][51]['training']['epochs']=[]
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.8788015842437744})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 2.499415874481201})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 2.822906494140625})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 2.954557180404663})
store['active_learning_steps'][51]['training']['best_epoch']=1
store['active_learning_steps'][51]['evaluation_metrics']={'accuracy': 0.6117, 'crossentropy': 1.9138431640625}
store['active_learning_steps'][51]['acquisition']={'indices': [['id', 6955], ['id', 21196], ['id', 50538], ['id', 9709], ['id', 5982]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.1804496632370611, 2.1191461800445537, 2.8158268546061063, 3.37302508576966, 3.7656239896101464]}
store['active_learning_steps'].append({})
store['active_learning_steps'][52]['training']={}
store['active_learning_steps'][52]['training']['epochs']=[]
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 1.9023357629776})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 2.7272071838378906})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 2.985440731048584})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 3.4826531410217285})
store['active_learning_steps'][52]['training']['best_epoch']=1
store['active_learning_steps'][52]['evaluation_metrics']={'accuracy': 0.5832, 'crossentropy': 2.1023052734375}
store['active_learning_steps'][52]['acquisition']={'indices': [['id', 58394], ['id', 59747], ['id', 43904], ['id', 3634], ['id', 24722]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.2621363925986113, 2.2160914963889056, 2.982404408606093, 3.562030863618804, 3.9426129261942187]}
store['active_learning_steps'].append({})
store['active_learning_steps'][53]['training']={}
store['active_learning_steps'][53]['training']['epochs']=[]
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 1.9125149250030518})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 2.5102596282958984})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 2.8320212364196777})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 3.040459632873535})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 3.148341655731201})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 3.2816834449768066})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 3.458883047103882})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 3.3897106647491455})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 3.5022060871124268})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.664551258087158})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.489063262939453})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 3.1681571006774902})
store['active_learning_steps'][53]['training']['best_epoch']=9
store['active_learning_steps'][53]['evaluation_metrics']={'accuracy': 0.6187, 'crossentropy': 3.7428890625}
store['active_learning_steps'][53]['acquisition']={'indices': [['id', 8964], ['id', 21401], ['id', 8681], ['id', 36329], ['id', 40586]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.6325565741081567, 2.826929281692273, 3.6497830678629875, 4.126294932552769, 4.382590448496961]}
store['active_learning_steps'].append({})
store['active_learning_steps'][54]['training']={}
store['active_learning_steps'][54]['training']['epochs']=[]
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 1.7233715057373047})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 2.331369400024414})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 2.39184832572937})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.6087088584899902})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 3.2234110832214355})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 3.0693907737731934})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 3.1954712867736816})
store['active_learning_steps'][54]['training']['best_epoch']=4
store['active_learning_steps'][54]['evaluation_metrics']={'accuracy': 0.6301, 'crossentropy': 2.8848302734375}
